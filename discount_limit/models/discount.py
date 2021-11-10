from odoo import fields, models
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT, DEFAULT_SERVER_DATE_FORMAT
from datetime import datetime


class DiscountLimit(models.TransientModel):
    _inherit = 'res.config.settings'

    max_disc_limit = fields.Monetary(string='Discount Limit', store=True)


class SaleOrderInherit(models.Model):
    _inherit = 'sale.order'

    def action_confirm(self):
        current_month = datetime.now().month
        print(current_month)
        records = (self.env['sale.order'].search([(datetime.strptime(
            str('date_order'), '%Y-%m-%d %H:%M:%S').month, '=', current_month)]))
        for rec in records:
            print(rec)
        result = super(SaleOrderInherit, self).action_confirm()
        return result
