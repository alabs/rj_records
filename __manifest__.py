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

    'depends': [
        'account',
        'base',
        'crm',
        'hr_timesheet',
        'l10n_es',
        'project',
        'project_task_default_stage'
    ],

    'data': [
        'security/rj_records_security.xml',
        'security/ir.model.access.csv',
        'views/assets.xml',
        'views/rj_menu.xml',
        'views/expedient_views.xml',
        'views/project_views.xml',
        'views/crm_views.xml',
        'views/menu_view.xml',
        'data/sequences.xml',
        'data/default_stages.xml',
        'data/crm_stage_data.xml',
        'data/areas_data.xml',
        'data/subject_data.xml',
        'data/sources_data.xml',
    ],

    'demo': [
    ],
}
