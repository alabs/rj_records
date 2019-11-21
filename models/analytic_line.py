# -*- coding: utf-8 -*-

import logging
_logger = logging.getLogger(__name__)
from odoo import api, fields, models, _


class AnalyticLine(models.Model):
    _inherit = 'account.analytic.line'
    _name = 'account.analytic.line'

    @api.onchange("amount", "project_id")
    def update_project(self):
        for line in self:
            project = line.project_id
            _logger.info("===================== Cargando proyecto {}".format(project.name))
            project._compute_amount_hours
