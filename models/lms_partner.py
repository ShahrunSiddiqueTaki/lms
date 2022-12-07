from odoo import models, fields, api


class lms_res_partner(models.Model):
    _inherit = "res.partner"

    # lms_partner_id = fields.Many2one('res.partner', ondelete='cascade')