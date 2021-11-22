odoo.define('pos_spanish_product.spanish_name', function(require)) {
"use strict";
var models = require('point_of_sale.models');
var _super_orderline = models.Orderline.prototype;
console.log("models",models);
models.load_fields('product.product', 'spanish_name');
models.Orderline = models.Orderline.extend({
    initialize: function(attr,options) {
         var line = _super_orderline.initialize.apply(this.arguments);
         this.spanish_name = this.product.spanish_name;
         console.log("spanish_name", this.spanish_name);
         }
    })
});