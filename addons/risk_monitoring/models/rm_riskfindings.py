# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import base64
from random import choice
from string import digits
from werkzeug.urls import url_encode

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError, AccessError
from odoo.modules.module import get_module_resource


class RiskFindings(models.Model):
    _name = "rm.RiskFindings"
    _description = "Findings of Asset Risks"
    _order = 'name'

    risk_ID = fields.Char()
    name = fields.Char(string="Employee Name", related='resource_id.name', store=True, readonly=False, tracking=True)
    FindingDate = fields.date("Date of Findings")
    note = fields.Text('Note')

    Asset_name = fields.Many2one('rm.InvestedAssets', 'Asset_ID','Asset Name')