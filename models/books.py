from odoo import models, fields, api
import requests
import base64
import re
from odoo.exceptions import ValidationError


class books(models.Model):
    _name = 'lms.books'
    _description = 'Book Description'
    _rec_name = "book_name"
    # _inherit = 'product.template'

    book_name = fields.Char(string="Book Name")
    book_price = fields.Float()
    book_page = fields.Integer()
    book_ISBN = fields.Char(string="ISBN")
    create_book_isbn = fields.Char(string="ISBN")
    book_description = fields.Text()

    book_image = fields.Binary("Image")
    avalability = fields.Selection([('aval', ' Available'),
                                    ('notaval', 'Not Available')
                                    ], string='Avalability')

    # Relation
    author_name = fields.Many2many('lms.authors', string="Author Name")
    publisher = fields.Many2one('lms.publishers', string="Publisher Name")
    book_category = fields.Many2many('lms.categories', string="Category")

    lms_employee_id = fields.Many2one('hr.employee', string="Responsible", ondelete='cascade')

    def create_book_form(self):
        view_id = self.env.ref('lms.create_book_isbn').id
        context = self._context.copy()

        return {
            'name': 'search.hotel.form',
            'view_type': 'form',
            'view_mode': 'tree',
            'views': [(view_id, 'form')],
            'res_model': 'lms.books',
            'view_id': view_id,
            'type': 'ir.actions.act_window',
            'res_id': self.id,
            'target': 'new',
            'context': context,
        }

    @api.depends("create_book_isbn", "book_name", "author_name")
    def create_book_btn(self):
        x = self.create_book_isbn
        result = requests.get('https://openlibrary.org/search.json?isbn=' + x)
        self.book_name = result.json()["docs"][0]["title"]

        image_link = str(result.json()["docs"][0]["cover_i"])
        img_url = "https://covers.openlibrary.org/b/id/" + image_link + "-M.jpg"
        img = base64.b64encode(requests.get(img_url).content)
        self.book_image = img

        self.book_description = result.json()["docs"][0]["first_sentence"]
        au_name = result.json()["docs"][0]["author_name"][0]
        self.book_ISBN = x
        print(au_name)
        # self.author_name = [(4, au_name)]

        # self.publisher = str(result.json()["docs"][0]["publisher"][0])

        print(result.json()["docs"][0]["title"])

    _sql_constraints = [
        ('book_ISBN', 'unique (book_ISBN)', 'Book already exists!!')]
