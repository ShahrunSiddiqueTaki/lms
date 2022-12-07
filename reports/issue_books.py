# from odoo import api, models, _


# class IssueBookReport(models.AbstractModel):
#     _name = 'report.lms.issuebook_report'
#     _description = 'Issue Book Report'

#     @api.model
#     def _get_report_values(self, docids, data=None):
#         if data['form']['book']:
#             appointments = self.env['lms.issue.books'].search([('book', '=', data['form']['patient_id'][0])])
#         else:
#             appointments = self.env['lms.issue.books'].search([])
#         # appointment_list = []
#         # for app in appointments:
#         #     vals = {
#         #         'name': app.name,
#         #         'notes': app.notes,
#         #         'appointment_date': app.appointment_date
#         #     }
#         #     appointment_list.append(vals)
#         return {
#             'doc_model': 'hospital.patient',
#             'appointments': appointments,
#         }