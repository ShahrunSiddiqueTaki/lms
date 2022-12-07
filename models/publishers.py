from odoo import models, fields, api


class publishers(models.Model):
    _name = 'lms.publishers'
    _description = 'Publication Description'
    _rec_name = "publisherName"

    publisherName = fields.Char(string="Publisher Name")
    publisherImage = fields.Binary("Image")
    totalBooks = fields.Integer(string="Total Books")
    bookList = fields.One2many('lms.books','publisher',string='Book List')

    
   
