from odoo import api, fields, models


class HospitalMedicine(models.Model):
    _name = "hospital.medicine"
    _description = "Hospital Medicine"

    name = fields.Char(string='Medicine', required='True')
