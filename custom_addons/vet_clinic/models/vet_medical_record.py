from odoo import models, fields, api
from odoo.exceptions import UserError

class VetMedicalRecord(models.Model):
    _name = 'vet.medical.record'
    _description = 'Hồ sơ khám bệnh'

    name = fields.Char('Mã hồ sơ', required=True, default='New', copy=False)
    patient_id = fields.Many2one('vet.patient', string='Thú cưng', required=True)
    appointment_id = fields.Many2one('vet.appointment', string='Lịch hẹn', domain="[('patient_id', '=', patient_id)]")
    doctor_id = fields.Many2one('res.users', string='Bác sĩ', default=lambda self: self.env.uid)
    date = fields.Date('Ngày khám', default=fields.Date.context_today)
    symptom = fields.Text('Triệu chứng')
    diagnosis = fields.Text('Chẩn đoán')
    treatment = fields.Text('Điều trị')
    service_ids = fields.Many2many('vet.service', string='Dịch vụ')
    invoice_id = fields.Many2one('account.move', string='Hóa đơn')
    state = fields.Selection([
        ('draft', 'Dự thảo'),
        ('confirmed', 'Đã xác nhận'),
        ('done', 'Đã hoàn thành'),
        ('invoiced', 'Đã lập hóa đơn')
    ], string='Trạng thái', default='draft')

    @api.model
    def create(self, vals):
        if vals.get('name') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('vet.medical.record') or 'New'
        return super().create(vals)

    def action_confirm(self):
        for record in self:
            if record.state != 'draft':
                raise UserError("Chỉ có thể xác nhận khi trạng thái là 'Dự thảo'")
        self.write({'state': 'confirmed'})

    def action_done(self):
        for record in self:
            if record.state != 'confirmed':
                raise UserError("Chỉ có thể xác nhận khi trạng thái là 'Đã xác nhận'")
        self.write({'state': 'done'})

    def action_create_invoice(self):
        if not self.service_ids:
            raise UserError('Chưa chọn dịch vụ để tạo hóa đơn.')

        for record in self:
            if record.state != 'done':
                raise UserError("Chỉ có thể xác nhận khi trạng thái là 'Đã hoàn thành'")

        return {
            'type': 'ir.actions.act_window',
            'res_model': 'vet.medical.record.invoice.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {
                'active_id': self.id,
            }
        }
