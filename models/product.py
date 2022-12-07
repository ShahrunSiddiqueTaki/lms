from odoo import models, fields


class Shop(models.Model):
    _inherit = 'product.template'
    _description = 'Product Add'

    name = fields.Char(string="Product Name")
    price = fields.Float(string="Price")
    image = fields.Binary(string='Photo', attachment=True)
