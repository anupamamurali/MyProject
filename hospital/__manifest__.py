{
    'name': 'Hospital Management',
    'version': '14.0.5.0.0',
    'summary': 'Hospital Management Application',
    'sequence': -100,
    'description': """Hospital Management Application""",
    'category': 'Hidden',
    'website': '',
    'depends': [
        'contacts',
        'base',
        'account',
        'mail'
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/data.xml',
        'wizard/patient_report_view.xml',
        'views/partner_view.xml',
        'views/doctor_view.xml',
        'views/patient_card.xml',
        'views/op.xml',
        'views/consult.xml',
        'views/disease.xml',
        'views/appointment.xml'
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
