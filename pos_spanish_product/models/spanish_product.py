from odoo import fields, models


class SpanishProduct(models.Model):
    _inherit = 'product.template'

    spanish_name = fields.Char(string='Spanish Name')