from odoo import models, fields, api

class lms_employee(models.Model):
    _inherit = "hr.department"

    # _inherits = {"res.users": "res.parter"}

    lms_employee_id = fields.Many2one('hr.employee', ondelete='cascade')