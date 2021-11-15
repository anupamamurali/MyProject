# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'School Management',
    'version' : '1.0',
    'summary': 'School Management Software',
    'sequence': 10,
    'description': """School Management Software""",
    'category': 'Hidden',
    'website': '',
    'depends': [],
    'data': [
        'security/ir.model.access.csv',
        'views/student.xml',
        'report/report.xml',
        'report/student_details.xml'
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
