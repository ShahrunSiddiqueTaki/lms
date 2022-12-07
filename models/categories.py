from odoo import models, fields, api


class categories(models.Model):
    _name = 'lms.categories'
    _description = 'Category Description'
    _rec_name = "category_name"

    category_name = fields.Char(string="Category Name")
    book_list = fields.Many2many('lms.books',string='Book List')
    book_count = fields.Integer(string="Total Book", compute="_get_book_count", store="True")

    @api.depends("book_list")
    def _get_book_count(self):
        for r in self:
            r.book_count = len(r.book_list)
    
   
