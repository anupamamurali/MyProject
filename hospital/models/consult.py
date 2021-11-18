from odoo import fields, models
from datetime import datetime


class HospitalConsult(models.Model):
    _name = "hospital.consult"
    _description = "Hospital Consultation"

    patient_card = fields.Many2one('hospital.patient.card',
                                   string='Patient Card', required=True)
    name = fields.Many2one(string='Patient Name',
                           related='patient_card.patient_name')
    consult_type = fields.Selection([('op', 'OP'), ('ip', 'IP')])
    doctor = fields.Many2one('hr.employee',
                             domain="[('job_position','=','Doctor')]")
    department = fields.Many2one(string='Department',
                                 related='doctor.department_id')
    date = fields.Date(string='Date', default=datetime.today())
    disease = fields.Many2one('hospital.disease', string='Disease',
                              required=True)
    description = fields.Text(string='Description')
    prescription_line_ids = fields.One2many('consult.prescription.lines',
                                            'consult_id',
                                            string='Prescription Lines')


class ConsultPrescriptionLines(models.Model):
    _name = "consult.prescription.lines"
    _description = "Consultation Prescription Lines"

    name = fields.Many2one('hospital.medicine', string='Medicine', required=True)
    consult_id = fields.Many2one('hospital.consult', string='Consult')
    dose = fields.Integer(string='Dose')
    days = fields.Integer(string='Days')
    note = fields.Text(string='Description')
