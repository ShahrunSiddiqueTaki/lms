from odoo import models, fields, api


class lms_typemember(models.Model):
    _name = 'lms.typemember'
    _description = 'Member Types'
    _rec_name = "member_types"

    member_types = fields.Selection(
    selection=[
        ("monthly", "Monthly"),
        ("yearly", "Yearly")
    ],
    string="Member Types",
    copy=False,
)
    fees = fields.Float(string="Fees")