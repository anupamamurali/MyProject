{
    'name': 'Product Available Quantity',
    'version': '14.0.1.0.0',
    'summary': 'Product Available Quantity',
    'sequence': -100,
    'description': """Product Available Quantity In POS""",
    'category': 'Hidden',
    'website': '',
    'depends': [
        'point_of_sale',
        'product',
        'stock'
    ],
    'data': [
        'views/pos_location.xml',
        'views/assets.xml'
    ],
    'demo': [],
    'qweb': [
        'static/src/xml/prod_avail.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
