from odoo import models, fields


class ProductBrand(models.Model):

    _inherit = 'product.template'

    brand = fields.Char(string="Brand")
