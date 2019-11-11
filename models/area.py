# -*- coding: utf-8 -*-

from odoo import api, fields, models

class Area(models.Model):
    _name = 'rj_records.area'
    name = fields.Char(required=True, size=30)
