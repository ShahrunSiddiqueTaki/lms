from odoo import models, fields, api

class MemberIssueBooks(models.Model):
    
    _inherit = 'lms.members'

    issued_books = fields.One2many('lms.issue.books','member', string = "Book List")