from odoo import models, fields, api
from odoo.exceptions import UserError


class VetInvoice(models.Model):
    _name = 'vet.invoice'
    _description = 'Hóa đơn thú y'

    name = fields.Char('Mã hóa đơn', required=True, default='New', copy=False)
    medical_record_id = fields.Many2one('vet.medical.record', string='Hồ sơ khám')
    invoice_id = fields.Many2one('account.move', string='Hóa đơn kế toán', domain=[('move_type', '=', 'out_invoice')])
    state = fields.Selection(related='invoice_id.payment_state', string='Tình trạng thanh toán', store=True, readonly=True)
    partner_id = fields.Many2one(related='invoice_id.partner_id', string='Khách hàng', store=True)
    amount_total = fields.Monetary(related='invoice_id.amount_total', string='Tổng tiền', store=True)
    currency_id = fields.Many2one(related='invoice_id.currency_id', string='Tiền tệ', store=True)
    note = fields.Text('Ghi chú')

    def open_invoice(self):
        for record in self:
            if not record.invoice_id:
                raise UserError("Chỉ có thể xác nhận khi có Hóa đơn kế toán")

        return {
            'type': 'ir.actions.act_window',
            'res_model': 'account.move',
            'res_id': self.invoice_id.id,
            'view_mode': 'form',
            'target': 'current',
        }

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('vet.invoice') or 'New'
        return super().create(vals)
