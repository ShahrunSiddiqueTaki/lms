from odoo import models, fields, api


class awards(models.Model):
    _name = 'lms.awards'
    _description = 'Awaerd Description'

    award_name = fields.Char(string="Awards Name")
    award_image = fields.Binary("Image")
    author_list = fields.Many2many('lms.authors',string='Author List')
    book_list = fields.Many2many('lms.books',string='Book List')
    
   
