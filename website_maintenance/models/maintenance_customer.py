from odoo import fields, models, api


class CustomerView(models.Model):
    _inherit = "maintenance.request"
    _rec_name = 'rec_name'

    customer_name = fields.Char(string='Customer Name')
    rec_name = fields.Char(string='Rec Name', required=True, copy=False,
                           readonly=True, default=lambda self: 'New')

    @api.model
    def create(self, vals):
        """Sequence Generation"""
        if vals.get('rec_name', 'New') == 'New':
            vals['rec_name'] = self.env['ir.sequence'].next_by_code(
                'maintenance.request') or 'New'
        res = super(CustomerView, self).create(vals)
        return res