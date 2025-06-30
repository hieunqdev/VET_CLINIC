from odoo import models, fields, api
from odoo.exceptions import ValidationError

class VetAppointment(models.Model):
    _name = 'vet.appointment'
    _description = 'Lịch hẹn khám bệnh'

    name = fields.Char(string='Mã lịch hẹn', required=True, default='New', copy=False)
    patient_id = fields.Many2one('vet.patient', string='Thú cưng', required=True)
    owner_id = fields.Many2one(related='patient_id.owner_id', string='Chủ thú cưng', store=True)
    appointment_date = fields.Datetime('Thời gian hẹn', required=True)
    doctor_id = fields.Many2one('res.users', string='Bác sĩ phụ trách')
    state = fields.Selection([
        ('draft', 'Dự thảo'),
        ('confirmed', 'Đã xác nhận'),
        ('done', 'Hoàn thành'),
        ('cancelled', 'Đã hủy')
    ], default='draft', string='Trạng thái')

    note = fields.Text('Ghi chú')

    # nếu không nhập gì vào trường name, tự động gắn mã như trong data/ir_sequence_data.xml: APT/0001, APT/0002
    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('vet.appointment') or 'New'
        return super().create(vals)
