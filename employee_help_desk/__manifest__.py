{
    'name': 'Employee Help Desk',
    'version': '14.0.1.0.0',
    'summary': 'Employee Help Desk',
    'sequence': -100,
    'description': """Employee Help Desk""",
    'category': 'Hidden',
    'website': '',
    'depends': ['hr', 'website', 'mail', 'base'],
    'data': [
        'security/ir.model.access.csv',
        'data/data.xml',
        'views/help_desk.xml',
        'views/help_category.xml',
        'views/website_helpdesk.xml'
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
