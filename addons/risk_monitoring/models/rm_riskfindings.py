# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


from odoo import fields, models


class RiskFindings(models.Model):
    _name = "rm.riskfindings"
    _description = "Findings of Asset Risks"
    _order = 'name'

    risk_ID = fields.Char()
    name = fields.Char(string="Risk Description", store=True, readonly=False, tracking=True)
    FindingDate = fields.Date("Date of Findings")
    note = fields.Text('Note')

    #Asset_name = fields.Many2one('rm.investedassets', 'Asset_ID','Asset Name')