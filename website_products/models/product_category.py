from odoo import fields, models


class ProductCategory(models.Model):
    _inherit = "res.partner"

    product_ids = fields.Many2many('product.template', string='Allowed Products',
                                   help='It is used to show only the allowed '
                                        'products in shop')
    pro_cat_ids = fields.Many2many('product.public.category',
                                   string='Allowed Product Categories',
                                   help='It is used to show only the allowed '
                                        'product category in shop')
