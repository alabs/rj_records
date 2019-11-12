# -*- coding: utf-8 -*-

import logging
_logger = logging.getLogger(__name__)
from odoo import api, fields, models, _


class Lead(models.Model):
    _inherit = 'crm.lead'
    _name = 'crm.lead'

    @api.multi
    def create_project(self):
        """docstring for create_project"""
        _logger.info("Creating project")
        self.ensure_one()

        project_form = self.env.ref('project.project_project_view_form_simplified', False)

        ctx = dict(
            default_model='project.project',
            default_name=self.name,
            default_client_ids=[self.partner_id.id]
        )

        return {
            'name': _('Crear Proyecto'),
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'project.project',
            'views': [(project_form.id, 'form')],
            'view_id': project_form.id,
            'target': 'new',
            'context': ctx,
            }

