odoo.define('pos_avail_quant.invent_loc', function(require) {
"use strict";
var models = require('point_of_sale.models');
var rpc = require('web.rpc');
models.load_fields('pos.config','invent_loc_id');
var _super_product = models.PosModel.prototype;
models.PosModel = models.PosModel.extend({
    initialize: function(session, attributes) {
         _super_product.initialize.apply(this, arguments);
         console.log("Working");
         console.log(this.config_id);
         return rpc.query({
                    model: 'pos.config',
                    method: 'get_product_loc',
                    args: [this.config_id],
                }).then(function (products) {
                    console.log(products);
                    console.log("Testing");
                });
    }
});
});