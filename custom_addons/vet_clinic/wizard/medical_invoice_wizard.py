from odoo import models, fields, api
from odoo.exceptions import UserError

class VetMedicalRecordInvoiceWizard(models.TransientModel):
    _name = 'vet.medical.record.invoice.wizard'
    _description = 'Tạo hóa đơn từ hồ sơ khám'

    def create_invoice(self):
        medical_record = self.env['vet.medical.record'].browse(self.env.context.get('active_id'))
        if not medical_record:
            raise UserError("Không tìm thấy hồ sơ.")

        invoice_lines = []
        for service in medical_record.service_ids:
            invoice_lines.append((0, 0, {
                'name': service.name,
                'quantity': 1,
                'price_unit': service.price,
            }))

        invoice = self.env['account.move'].create({
            'move_type': 'out_invoice',
            'partner_id': medical_record.patient_id.owner_id.id,
            'invoice_line_ids': invoice_lines,
        })

        medical_record.write({
            'invoice_id': invoice.id,
            'state': 'invoiced',
        })

        self.env['vet.invoice'].create({
            'medical_record_id': medical_record.id,
            'invoice_id': invoice.id,
            'note': 'Tạo từ hồ sơ khám bệnh',
        })

        return {
            'type': 'ir.actions.act_window',
            'res_model': 'account.move',
            'res_id': invoice.id,
            'view_mode': 'form',
            'target': 'current',
        }
