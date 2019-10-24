# -*- coding: utf-8 -*-

from odoo import api, fields, models

FIELD_STATES = [
    ('open', 'Abierto'),
    ('closed', 'Cerrado'),
    ('sleep', 'Dormido')
]


class Expedient(models.Model):
    _inherit = 'project.project'
    _name = 'rj_records.expedient'
    name = fields.Char(required=True, size=30)
    code = fields.Char(
        compute='_compute_code',
        string='N° de Expediente',
        store=True
    )

    state = fields.Selection(
        selection=FIELD_STATES,
        string='Estado',
        readonly=True,
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
        string='Clientes'
    )

    managers_ids = fields.Many2many(
        'res.users',
        'expedient_managers_users_rel',
        'project_id',
        'user_id',
        string='Responsables'
    )

    def _compute_code(self):
        for record in self:
            year = datetime.strptime(
                record.date_start, DEFAULT_SERVER_DATE_FORMAT
            ).year
            record.code = record.id + "/" + year

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
