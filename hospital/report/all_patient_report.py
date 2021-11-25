# from odoo import api, fields, models
#
#
# class AllPatientReport(models.AbstractModel):
#     _name = 'report.hospital.report_all_patient_details'
#     _description = "Patient Report"
#
#     @api.model
#     def _get_report_values(self, docids, data=None):
#         print("Testing.....")
#         docs = self.env['hospital.patient.card'].search([])
#         return {
#             'docs': docs
#         }