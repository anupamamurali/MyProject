from odoo import api, fields, models


class HospitalDisease(models.Model):
    _name = "hospital.disease"
    _description = "Hospital Disease"

    name = fields.Char(string='Disease', required='True', translate=True)