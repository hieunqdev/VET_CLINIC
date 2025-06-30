from odoo import models, fields

class VetService(models.Model):
    _name = 'vet.service'
    _description = 'Dịch vụ y tế'

    name = fields.Char('Tên dịch vụ', required=True)
    price = fields.Float('Giá', required=True)
