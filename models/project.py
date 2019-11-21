# -*- coding: utf-8 -*-

import logging
_logger = logging.getLogger(__name__)
from datetime import datetime
from odoo import api, fields, models

FIELD_STATES = [
    ('open', 'Abierto'),
    ('closed', 'Cerrado'),
    ('sleep', 'Dormido')
]

FIELD_TYPES = [
    ('particular', 'Particular'),
    ('turno', 'Turno de oficio'),
    ('probono', 'Probono')
]

FIELD_COMPLEXITY = [
    ('0', 'Ninguna'),
    ('1', 'Muy Baja'),
    ('2', 'Baja'),
    ('3', 'Media'),
    ('4', 'Alta'),
    ('5', 'Muy Alta')
]


class Project(models.Model):
    _inherit = 'project.project'
    _name = 'project.project'
    _rec_name = 'code'

    name = fields.Char(required=True, size=60)

    code = fields.Char(
        string='N° de Expediente'
    )

    state = fields.Selection(
        [('open', 'Abierto'), ('closed', 'Cerrado'), ('sleep', 'Dormido')],
        string='Estado',
        default='open'
    )

    partner_id = fields.Many2one(
        'res.partner',
        string='Pagador',
        auto_join=True,
        track_visibility='onchange'
    )

    client_ids = fields.Many2many(
        'res.partner',
        'expedient_clients_rel',
        'project_id',
        'partner_id',
        required=True,
        string='Clientes'
    )

    managers_ids = fields.Many2many(
        'res.users',
        'expedient_managers_users_rel',
        'project_id',
        'user_id',
        required=True,
        string='Responsables'
    )

    complexity = fields.Selection(
        selection=FIELD_COMPLEXITY,
        string='Complejidad',
        required=True,
        default='1'
    )

    source_id = fields.Many2one(
        'rj_records.source',
        string='Origen del asunto',
        auto_join=True,
        required=True,
        track_visibility='onchange'
    )

    lead_id = fields.Many2one(
        'crm.lead',
        string='CRM',
        readonly=True,
        auto_join=True,
        track_visibility='onchange'
    )

    area_id = fields.Many2one(
        'rj_records.area',
        string='Area',
        auto_join=True,
        required=True,
        track_visibility='onchange'
    )

    subject_id = fields.Many2one(
        'rj_records.subject',
        string='Asunto',
        auto_join=True,
        required=True,
        track_visibility='onchange'
    )

    type = fields.Selection(
        selection=FIELD_TYPES,
        required=True,
        string='Tipo'
    )

    procurer = fields.Char(
        size=30,
        string='Procurador'
    )

    currency_id = fields.Many2one(
        'res.currency',
        string='Currency',
        related='company_id.currency_id',
        readonly=True
    )

    revenue = fields.Monetary(
        'Honorarios Pactados',
        currency_field='currency_id',
        tracking=True
    )

    expense_ids = fields.One2many(
        'hr.expense',
        'project_id',
        string='Gastos'
    )

    invoice_ids = fields.One2many(
        'account.invoice',
        'project_id',
        string='Facturas'
    )

    amount_earned = fields.Monetary(
        'Ingresos',
        currency_field='currency_id',
        compute='_compute_amount_earned',
    )

    amount_expensed = fields.Monetary(
        'Gastos',
        currency_field='currency_id',
        compute='_compute_amount_expensed',
    )

    amount_hours =  fields.Monetary(
        'Costo en horas',
        currency_field='currency_id',
        compute='_compute_amount_hours',
    )

    amount_total = fields.Monetary(
        'Balance',
        currency_field='currency_id',
        compute='_compute_amount_total',
    )

    def _compute_amount_hours(self):
        for project in self:
            amount_hours = sum(line.amount for line in project.analytic_account_id.line_ids)
            project.amount_hours = amount_hours

    def _compute_amount_earned(self):
        for record in self:
           record.amount_earned = sum(line.amount_untaxed for line in record.invoice_ids)

    def _compute_amount_expensed(self):
        for record in self:
           record.amount_expensed = 0 - sum(line.total_amount for line in record.expense_ids)

    def _compute_amount_total(self):
        for record in self:
           record.amount_total = record.amount_earned + record.amount_expensed + record.amount_hours

    def close_project(self):
        for rec in self:
            rec.state = "closed"

    def open_project(self):
        for rec in self:
            rec.state = "open"

    @api.multi
    def name_get(self):
        result = []
        for record in self:
            rec_name = "{} - {}".format(record.code, record.name)
            result.append((record.id, rec_name))
        return result

    @api.model
    def create(self, vals):
        code = self.env['ir.sequence'].next_by_code('rj_records.files') or '/'
        vals['code'] = code
        return super(Project, self).create(vals)
