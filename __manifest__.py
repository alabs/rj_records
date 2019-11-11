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

    'depends': ['base', 'project', 'project_task_default_stage'],

    'data': [
        'security/rj_records_security.xml',
        'security/ir.model.access.csv',
        'views/rj_menu.xml',
        'views/expedient_views.xml',
        'views/project_views.xml',
        'data/sequences.xml',
        'data/default_stages.xml',
    ],

    'demo': [
    ],
}
