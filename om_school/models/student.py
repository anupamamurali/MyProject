# -*- coding: utf-8 -*-
from odoo import api, fields, models, _, tools
from odoo.osv import expression
from odoo.exceptions import UserError, ValidationError
from odoo import api, fields, models

class SchoolStudent(models.Model):
    _name = "school.student"
    _description = "School Student"

    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age', required=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('others', 'Others'),
    ], required=True)
    note = fields.Text(string='Description')