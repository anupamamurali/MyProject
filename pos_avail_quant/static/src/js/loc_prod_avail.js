odoo.define('pos_avail_quant.invent_loc', function(require) {
"use strict";
var models = require('point_of_sale.models');
var rpc = require('web.rpc');
models.load_fields('pos.config','invent_loc_id');
var _super_product = models.PosModel.prototype;
models.load_models([{
    model:  'stock.quant',
    fields: ['product_id', 'location_id', 'available_quantity'],
    domain: function(self) {return [['location_id', '=', self.config.invent_loc_id[0]]];},
    loaded: function(self, quantities) {
        self.quantities = quantities;
        self.quantities_by_id = {};
        self.quantities.forEach(function(quantity) {
                self.db.product_by_id[quantity.product_id[0]].available_qty=quantity.available_quantity;
                console.log(self.db.product_by_id[quantity.product_id[0]].available_qty);
//                self.quantities_by_id[quantity.id] = quantity;
//                console.log(quantity.product_id[0]);
        });
    }
}])
});