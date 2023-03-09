{
    'name': 'Product Brand',
    'sequence': 1,
    'version': '16.0.1.0.0',
    'depends': ['base','sale', 'point_of_sale'],

    'data':  [
              'views/product_brand.xml',
              ],
    'assets': {
       'point_of_sale.assets': [
           'pos_product_brand/static/src/js/pos_brand_reciept.js',
           'pos_product_brand/static/src/xml/pos_brand_order_line.xml',
           'pos_product_brand/static/src/xml/pos_brand_reciept.xml',
       ],
    },

    'installable': True,
    'application': True,
    'auto_install': False,

}
