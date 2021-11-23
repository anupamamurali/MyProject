odoo.define('pos_spanish_product.spanish_name', function(require) {
"use strict";
console.log("working");
var models = require('point_of_sale.models');
var _super_product = models.PosModel.prototype;
console.log("models",models);
models.PosModel = models.PosModel.extend({
    initialize: function(session, attributes) {
         var self = this;
         models.load_fields('product.product', ['spanish_name']);
         _super_product.initialize.apply(this, arguments);
         console.log("hi")
         }
    });
});