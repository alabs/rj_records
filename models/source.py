# -*- coding: utf-8 -*-

from odoo import api, fields, models

class Source(models.Model):
    _name = 'rj_records.source'
    name = fields.Char(required=True, size=30)
