# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class InvestedAssets(models.Model):
    _name = "rm.investedassets"
    _description = "Invested Asset list"
    _rec_name = "name"
    _order = "DateInvested"

    Asset_ID = fields.Id('Asset ID')
    name = fields.Char('Department Name', required=True)
    active = fields.Boolean('Active', default=True)
    InvAmount = fields.Integer('Invested Amount')
    DateInvested = fields.Date("Date of Investment")

    #risk_ID = fields.One2many('rm.RiskFindings','risk_ID', 'Various Risk findings')

    """
    parent_id = fields.Many2one('hr.department', string='Parent Department', index=True, domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]")
    child_ids = fields.One2many('hr.department', 'parent_id', string='Child Departments')
    manager_id = fields.Many2one('hr.employee', string='Manager', tracking=True, domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]")
    member_ids = fields.One2many('hr.employee', 'department_id', string='Members', readonly=True)
    """

