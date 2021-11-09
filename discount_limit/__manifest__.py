{
    'name': 'Discount Limit',
    'version': '14.0.1.0.0',
    'summary': 'Discount Limit',
    'sequence': -100,
    'description': """Discount Limit""",
    'category': 'Hidden',
    'website': '',
    'depends': [
        'sale_management'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/discount.xml'
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
