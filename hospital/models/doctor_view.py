from odoo import fields, models


class DoctorView(models.Model):
    _inherit = "hr.employee"

    is_doctor = fields.Boolean(string='Is Doctor')
    currency_id = fields.Many2one('res.currency', string='Currency')
    fee = fields.Monetary(string='Fee')
