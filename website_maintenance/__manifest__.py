{
    'name': 'Website Maintenance Request',
    'version': '14.0.1.0.0',
    'summary': 'Website Maintenance Request',
    'sequence': -100,
    'description': """Maintenance In Website""",
    'category': 'Hidden',
    'website': '',
    'depends': [
        'website',
        'website_sale',
        'maintenance',
        'mail'
    ],
    'data': [
        'data/data.xml',
        'views/website_form.xml',
        'views/maintenance_customer.xml'
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
