from odoo import fields, models


class DiscountLimit(models.TransientModel):
    _inherit = 'res.config.settings'
    _name = 'discount.limit'

    max_disc_limit = fields.Integer(string='Maximum Discount Limit')
