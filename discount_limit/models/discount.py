from odoo import api, fields, models
from odoo.exceptions import UserError
from datetime import datetime
from dateutil.relativedelta import relativedelta
import calendar


class DiscountLimit(models.TransientModel):
    _inherit = 'res.config.settings'

    monthly_discount = fields.Boolean(string='Monthly Discount Limit', config_parameter='discount_limit.monthly_discount')
    max_disc_limit = fields.Monetary(string='Maximum Discount')

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
        monthly_discount = self.env['ir.config_parameter'].sudo().get_param('discount_limit.monthly_discount') or False
        if monthly_discount:
            year = self.date_order.year
            month = self.date_order.month
            days_count = (calendar.monthrange(year, month))[1]
            print((datetime.today() + relativedelta(day=days_count)).strftime('%Y-%m-%d'))
            records = self.env['sale.order'].search([('date_order',
                  '<=', (datetime.today() + relativedelta(day=days_count)).strftime('%Y-%m-%d')),
                     ('date_order', '>=', (datetime.today()-relativedelta(day=1)).strftime('%Y-%m-%d'))])
            total = 0
            for rec in records:
                for line in rec.order_line:
                    unit_price = line.price_unit
                    total_price = unit_price * line.product_uom_qty
                    sub_total = line.price_subtotal
                    discount = total_price - sub_total
                    total += discount
            limit = self.env['ir.config_parameter'].sudo().get_param('discount_limit.max_disc_limit') or False
            if total > float(limit):
                raise UserError("Warning...! Discount exceed the limit")
        result = super(SaleOrderInherit, self).action_confirm()
        return result
