odoo.define('pos_spanish_product.spanish_name', function(require) {
"use strict";
var models = require('point_of_sale.models');
var _super_product = models.PosModel.prototype;
models.PosModel = models.PosModel.extend({
    initialize: function(session, attributes) {
         models.load_fields('product.product', 'spanish_name');
         _super_product.initialize.apply(this, arguments);
         }
    });
});