# -*- coding: utf-8 -*-
{
    'name': 'Vet Clinic Management',
    'version': '1.0',
    'summary': 'Quản lý phòng khám thú cưng',
    'description': """
        Module quản lý phòng khám thú y, bao gồm:
        - Quản lý thú cưng
        - Lịch hẹn khám bệnh
        - Hồ sơ khám bệnh
        - Dịch vụ y tế và hóa đơn
        - Tích hợp với POS, Website, và API
    """,
    'author': 'Hiếu Dev',
    'website': '',
    'category': 'Healthcare',
    'depends': ['base', 'sale', 'account', 'stock', 'point_of_sale', 'website'],
    'data': [
        'data/ir_sequence_data.xml',
        'views/vet_menus.xml',
        'views/vet_patient_views.xml',
        'views/vet_appointment_views.xml',
        'views/vet_medical_record_views.xml',
        'views/vet_invoice_views.xml',
        'wizard/medical_invoice_wizard_view.xml',
    ],
    'assets': {

    },
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
