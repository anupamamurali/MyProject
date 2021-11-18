from odoo import fields, models


class HospitalDisease(models.Model):
    _name = "hospital.disease"
    _description = "Hospital Disease"

    name = fields.Char(string='Disease', required='True')
