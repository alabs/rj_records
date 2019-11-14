# -*- coding: utf-8 -*-

import logging
_logger = logging.getLogger(__name__)
from odoo import api, fields, models, _


class Lead(models.Model):
    _inherit = 'crm.lead'
    _name = 'crm.lead'

    project_id = fields.Many2one(
            'project.project',
            compute="_compute_project"
            )

    @api.multi
    def create_project(self):
        """docstring for create_project"""
        _logger.info("Creating project")
        self.ensure_one()

        project_form = self.env.ref('project.project_project_view_form_simplified', False)

        ctx = dict(
            default_model='project.project',
            default_lead_id=self.id,
            default_name=self.name,
            default_client_ids=[self.partner_id.id],
            default_revenue=self.planned_revenue
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

    @api.multi
    def open_project(self):
        """docstring for open_project"""
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'project.project',
            'res_id': self.project_id.id,
            }

    @api.multi
    def _compute_project(self):
        _logger.info("Buscando proyectos")
        projects = self.env['project.project']
        for record in self:
            project_got = projects.search([('lead_id', "=", record.id)])
            for project in project_got:
                record.project_id = project.id
                _logger.info("Tenemos proyecto")
