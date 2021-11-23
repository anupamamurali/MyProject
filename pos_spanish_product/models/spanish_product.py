from odoo import fields, models


class SpanishProduct(models.Model):
    _inherit = 'product.product'

    spanish_name = fields.Char(string='Spanish Name')