from odoo import fields, models, api


class PosLocation(models.Model):
    _inherit = 'pos.config'

    invent_loc_id = fields.Many2one('stock.location', string='Location',
                                    help='It is used to check the availability '
                                         'of product in the selected location.')

    def get_product_loc(self):
        print("In function")
        print(self)
        location_id = self.invent_loc_id.id
        print(location_id)
        product = self.env['stock.quant'].search([('location_id', '=',
                                                   location_id)])
        print(product)
        result = []
        for rec in product:
            print(rec.available_quantity)
            result.append(float(rec.available_quantity))
        print(result)
        return result
