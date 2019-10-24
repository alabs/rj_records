# -*- coding: utf-8 -*-

{
    'name': 'RJ Records',
    'summary': """Handle RJ expedient records for assign tasks and managers""",
    'description': """
    This module has functionalities inherid from odoo project manager with some
    extra functionalities that belongs to the RJ bussiness logic.
    """,
    'author': 'aLabs',
    'website': 'https://alabs.org',
    'category': 'Project',
    'license': 'AGPL-3',
    'version': '0.1',
    'installable': True,
    'application': True,

    'depends': ['base', 'project'],

    'data': [
        'views/expedient_views.xml',
    ],

    'demo': [
    ],
}
