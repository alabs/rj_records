# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

class Invoice(models.Model):
    _inherit = 'account.invoice'
    _name = 'account.invoice'

    project_id = fields.Many2one(
        'project.project',
        string='Expediente',
        auto_join=True,
        track_visibility='onchange'
    )

