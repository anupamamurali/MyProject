{
    'name': 'Spanish Product',
    'version': '14.0.1.0.0',
    'summary': 'Spanish Product ',
    'sequence': -100,
    'description': """Spanish Product Name""",
    'category': 'Hidden',
    'website': '',
    'depends': [
        'point_of_sale',
        'product'
    ],
    'data': [
        'views/spanish_name.xml',
        'views/assets.xml'
    ],
    'demo': [],
    'qweb': [
        'static/src/xml/product_spanish.xml',
        'static/src/xml/receipt_spanish.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
