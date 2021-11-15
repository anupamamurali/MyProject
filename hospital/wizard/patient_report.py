from odoo import api, fields, models


class PatientReportWizard(models.TransientModel):
    _name = "patient.report.wizard"
    _description = "Print Patient Wizard"

    patient_card = fields.Many2one('hospital.patient.card', string='Patient')
    date_from = fields.Date(string='Date From')
    date_to = fields.Date(string='Date To')
