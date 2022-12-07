
from odoo.exceptions import ValidationError
from odoo import models, fields, api
import re


class members(models.Model):
    _name = 'lms.members'
    _description = 'Members Description'
    _rec_name = 'member_name'

    member_name = fields.Char(string="Member Name", required="1")
    member_image = fields.Binary("Image")
    member_id = fields.Char(string="Member Id")
    member_email = fields.Char(string="Email", required="1")
    mobile = fields.Char(string="Mobile")
    gender = fields.Selection([('male', ' Male'), 
                                ('female', 'Female'),
                                ('others','Others')
                                ],string='Gender')
    book_on_hand = fields.One2many('lms.issue.books','member',string="Book List")
    # history = fields.Many2many('lms.books',string="History List")
    due = fields.Float('Total Due')
    address = fields.Char(string="Address")

    @api.constrains('member_email')
    def validate_mail(self):
        if self.member_email:
            check = re.match('^[a-zA-Z0-9]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', self.member_email)
            if check == None:
                raise ValidationError('Enter a valid E-mail')
    
   
