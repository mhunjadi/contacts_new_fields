# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ContactsInherited(models.Model):
    _inherit = 'res.partner'    

    new_field1 = fields.Boolean(string='OIB Is Mandatory', default=False)
    new_field2 = fields.Char(string='OIB', size=11)