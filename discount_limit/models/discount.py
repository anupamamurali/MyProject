from odoo import api, fields, models
from odoo.exceptions import UserError
from datetime import datetime
from dateutil.relativedelta import relativedelta


class DiscountLimit(models.TransientModel):
    _inherit = 'res.config.settings'

    max_disc_limit = fields.Monetary(string='Discount Limit')

    def set_values(self):
        super(DiscountLimit, self).set_values()
        select_type = self.env['ir.config_parameter'].sudo()
        select_type.set_param('discount_limit.max_disc_limit',
                              self.max_disc_limit)

    @api.model
    def get_values(self):
        res = super(DiscountLimit, self).get_values()
        select_type = self.env['ir.config_parameter'].sudo()
        update_val = select_type.get_param('discount_limit.max_disc_limit')
        res.update({'max_disc_limit': update_val})
        return res


class SaleOrderInherit(models.Model):
    _inherit = 'sale.order'

    def action_confirm(self):
        records = self.env['sale.order'].search([('date_order',
                  '<=', (datetime.today() + relativedelta(day=31)).strftime('%Y-%m-%d')),
                     ('date_order', '>=', (datetime.today()-relativedelta(day=1)).strftime('%Y-%m-%d'))])
        total = 0
        for rec in records:
            for line in rec.order_line:
                unit_price = line.price_unit
                total_price = unit_price * line.product_uom_qty
                sub_total = line.price_subtotal
                discount = total_price - sub_total
                total += discount
        print(total)
        limit = self.env['ir.config_parameter'].sudo().get_param('discount_limit.max_disc_limit') or False
        print(limit)
        if total > float(limit):
            raise UserError("Warning...! Discount exceed the limit")
        result = super(SaleOrderInherit, self).action_confirm()
        return result
