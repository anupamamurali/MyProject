from odoo import api, fields, models


class HelpCategory(models.Model):
    _name = "help.category"
    _description = "Employee Help Category"

    name = fields.Char(string='Help Request Category')