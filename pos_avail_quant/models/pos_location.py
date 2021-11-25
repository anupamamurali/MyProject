from odoo import fields, models


class PosLocation(models.Model):
    _inherit = 'pos.config'

    invent_loc = fields.Many2one('stock.location', string='Location', help='To select the location.')