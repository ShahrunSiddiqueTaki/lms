from odoo import models, fields, api


class authors(models.Model):
    _name = 'lms.authors'
    _description = 'Author Description'
    _rec_name = "author_name"

    author_name = fields.Char(string="Author Name")
    author_image = fields.Binary("Image")
    birth_date = fields.Date(string="Birth  Date testing")
    total_books = fields.Integer(string="Total Books")
    book_list = fields.Many2many('lms.books',string='Book List')
    gender = fields.Selection([('male', ' Male'), 
                                ('female', 'Female'),
                                ('others','Others')
                                ],string='Gender')
    awards = fields.Many2many('lms.awards',string='Awards')
    
   
