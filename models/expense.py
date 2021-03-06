# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class Expense(models.Model):
    _inherit = 'hr.expense'
    _name = 'hr.expense'

    project_id = fields.Many2one(
        'project.project',
        string='Expediente',
        auto_join=True,
        track_visibility='onchange'
    )

