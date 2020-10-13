# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Risk Monitoring',
    'version': '1.1',
    'category': 'Asset Management/Risk Monitoring',
    'sequence': 95,
    'summary': 'Risk Monitoring for all Assets',
    'description': "",
    'website': '',
    'depends': ['web'],
    'data': [
        'views/rm_assets_views.xml',
        'views/rm_riskfindings_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
