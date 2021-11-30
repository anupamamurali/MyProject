from odoo import fields, models, api


class PosLocation(models.Model):
    _inherit = 'pos.config'

    invent_loc_id = fields.Many2one('stock.location', string='Location',
                                    help='It is used to check the availability '
                                         'of product in the selected location.')
