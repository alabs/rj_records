# -*- coding: utf-8 -*-

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
    ('5', '5'),
    ('4', '4'),
    ('3', '3'),
    ('2', '2'),
    ('1', '1')
]


class Project(models.Model):
    _inherit = 'project.project'
    _name = 'project.project'

    name = fields.Char(required=True, size=30)

    code = fields.Char(
        string='N° de Expediente'
    )

    state = fields.Selection(
        selection=FIELD_STATES,
        string='Estado',
        readonly=False,
        required=True,
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

    @api.model
    def create(self, vals):
        code = self.env['ir.sequence'].next_by_code('rj_records.files') or '/'
        vals['code'] = code
        return super(Project, self).create(vals)

    @api.multi
    def action_close(self):
        '''Change expedient state to closed'''
        self.ensure_one()
        self.state = 'closed'

    @api.multi
    def action_sleep(self):
        '''Change expedient state to sleep'''
        self.ensure_one()
        self.state = 'sleep'
