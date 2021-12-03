{
    'name': 'Products And Product Categories',
    'version': '14.0.1.0.0',
    'summary': 'Allowed Products And Product Categories',
    'sequence': -100,
    'description': """Allowed Products And Product Categories In Website""",
    'category': 'Hidden',
    'website': '',
    'depends': [
        'website',
        'website_sale',
        'product',
        'base',
        'contacts'
    ],
    'data': [
        'views/product_category.xml'
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
