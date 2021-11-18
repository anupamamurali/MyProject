from odoo import fields, models


class PartnerView(models.Model):
    _inherit = "res.partner"
    dob = fields.Date(string='DOB')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('others', 'Others')
    ])




