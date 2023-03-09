console.log('lllllllllll')
odoo.define('pos_product_brand.pos_receipt', function(require){
    "use strict";
    var {Orderline} = require('point_of_sale.models');
    var Registries = require('point_of_sale.Registries');
    const CustomOrder = (Orderline)=>class CustomOrder extends Orderline {
        export_for_printing(){
            var result=super.export_for_printing(...arguments);
            result.brand=this.product.brand
            return result;
    }
    }
            Registries.Model.extend(Orderline ,CustomOrder);
});