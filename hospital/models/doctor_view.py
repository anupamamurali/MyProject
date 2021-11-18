from odoo import fields, models


class DoctorView(models.Model):
    _inherit = "hr.employee"

    job_position = fields.Char(string='Job Position')
    currency_id = fields.Many2one('res.currency', string='Currency')
    fee = fields.Monetary(string='Fee')
