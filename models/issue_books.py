from odoo import models, fields, api
from dateutil.relativedelta import relativedelta
import datetime
from datetime import timedelta
from odoo.exceptions import ValidationError


class issue_books(models.Model):
    _name = 'lms.issue.books'
    _description = 'Issue Description'

    book = fields.Many2many('lms.books',string='Book List')
    member = fields.Many2one('lms.members',string="Member Name")
    duration = fields.Integer(string="Duration", compute="_computed_duration", inverse="_inverse_duration")
    amount = fields.Integer(string="Fine")
    taking_date = fields.Date(string="Issue Date",default=lambda self: fields.Date.today())
    return_date = fields.Date(string="Return Date")
    issue_book_status = fields.Selection(
    selection=[
        ("issued", "Issued"),
        ("return", "Returned"),
        ("renew", "Renew"),
        ("due", "Due")
    ],
    string="Status",
    copy=False,
)
    issue_status_cal = fields.Integer()

    
    @api.constrains('return_date')
    def _check_return_date_t(self):
        if self.return_date < self.taking_date:
            raise ValidationError('Return date must be after Issue date.')

    @api.depends("taking_date", "return_date")
    def _computed_duration_t(self):
        for record in self:
            issued_date = record.taking_date
            currentDate = fields.Date.today()
            deadlineDate= record.return_date
            daysDiff = relativedelta(deadlineDate, issued_date)
            record.duration = daysDiff.day
            # dueday = relativedelta(currentDate, deadlineDate)
            # record.amount = dueday.days * 100

    def _inverse_duration_t(self):
        for record in self:
            issued_date = record.taking_date

            record.return_date = issued_date + datetime.timedelta(days= int(record.duration))

    @api.constrains('return_date')
    def _check_return_date(self):
        if self.return_date <= self.taking_date:
            raise ValidationError('Return date must be after Issue date.')

    @api.depends("taking_date", "return_date")
    def _computed_duration(self):
        for record in self:
            issued_date = record.taking_date
            currentDate = fields.Date.today()
            deadlineDate= record.return_date
            daysDiff = relativedelta(deadlineDate, issued_date)
            record.duration = daysDiff.days

    def _inverse_duration(self):
        for record in self:
            issued_date = record.taking_date

            record.return_date = issued_date + datetime.timedelta(days= int(record.duration))

    @api.onchange('amount')
    def onchange_amount(self):
        for record in self:
            issued_date = record.taking_date
            currentDate = fields.Date.today()
            deadlineDate= record.return_date
            daysDiff = relativedelta(currentDate, deadlineDate)
            record.amount = daysDiff.days * 100
            record.member.due = self.member.due+ record.amount

    def action_returned(self):
        for record in self:
            if record.issue_book_status == 'issued' or record.issue_book_status == 'due' or record.issue_book_status == 'renew':
                record.issue_book_status = 'return'
    
    def action_renew(self):
        for record in self:
            if record.issue_book_status == 'issued' or record.issue_book_status == 'due' or record.issue_book_status == 'return':
                record.issue_book_status = 'renew'

    def action_url(self):
        return{
            "type": "ir.actions.act_url",
            "url": "https://odoo.com",
            "target": "self",
        }

    
    # def action_status_calculation(self):
    #     for record in self:
    #         r = 0
    #         if record.issue_book_status == 'issued':
    #             r = r + 1
    #             record.issue_status_cal = r



 