# -*- coding: utf-8 -*-

from odoo import api, fields, models

class Subject(models.Model):
    _name = 'rj_records.subject'
    name = fields.Char(required=True, size=30)
    area_id = fields.Many2one(
        'rj_records.area',
        string='Area',
        auto_join=True,
        track_visibility='onchange'
    )
