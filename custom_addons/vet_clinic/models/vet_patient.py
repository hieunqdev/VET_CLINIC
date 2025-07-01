from odoo import models, fields

class VetPatient(models.Model):
    _name = 'vet.patient'
    _description = 'Thông tin thú cưng'

    name = fields.Char('Tên thú cưng', required=True)
    species = fields.Selection([
        ('dog', 'Chó'),
        ('cat', 'Mèo'),
        ('other', 'Khác')
    ], string='Loài', required=True)
    breed = fields.Char('Giống loài')
    gender = fields.Selection([
        ('male', 'Đực'),
        ('female', 'Cái')
    ], string='Giới tính')
    dob = fields.Date('Ngày sinh')
    owner_id = fields.Many2one('res.partner', string='Chủ sở hữu', required=True)
    color = fields.Char('Màu lông')
    image = fields.Binary('Ảnh thú cưng')

    medical_record_ids = fields.One2many('vet.medical.record', 'patient_id', string='Hồ sơ bệnh')
