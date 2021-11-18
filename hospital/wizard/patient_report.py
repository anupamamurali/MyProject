from odoo import api, fields, models


class PatientReportWizard(models.TransientModel):
    _name = "patient.report.wizard"
    _description = "Patient Report Wizard"

    patient_card = fields.Many2one('hospital.patient.card', string='Patient Id')
    patient_name = fields.Many2one(string='Patient Name',
                                   related='patient_card.patient_name')
    doctor = fields.Many2one('hr.employee',
                             domain="[('job_position','=','Doctor')]")
    department = fields.Many2one(string='Department',
                                 related='doctor.department_id')
    disease = fields.Many2one('hospital.disease', string='Disease')
    date_from = fields.Date(string='From Date')
    date_to = fields.Date(string='To Date')

    def create_patient_report(self):
        domain = []
        patient_card = self.patient_card
        if patient_card:
            domain += [('patient_card', '=', patient_card.id)]
        date_from = self.date_from
        if date_from:
            domain += [('date', '>=', date_from)]
        date_to = self.date_to
        if date_from:
            domain += [('date', '<=', date_to)]
        doctor = self.doctor
        if doctor:
            domain += [('doctor', '=', doctor.id)]
        department = self.department
        if department:
            domain += [('department', '=', department.id)]
        disease = self.disease
        if disease:
            domain += [('disease', '=', disease.id)]
        op = self.env['hospital.op'].search_read(domain)
        data = {
            'form_data': self.read()[0],
            'op': op
        }
        print(data)
        return self.env.ref('hospital.action_report_patient').report_action(self, data=data)

    def create_patient_excel_report(self):
        domain = []
        patient_card = self.patient_card
        if patient_card:
            domain += [('patient_card', '=', patient_card.id)]
        date_from = self.date_from
        if date_from:
            domain += [('date', '>=', date_from)]
        date_to = self.date_to
        if date_from:
            domain += [('date', '<=', date_to)]
        doctor = self.doctor
        if doctor:
            domain += [('doctor', '=', doctor.id)]
        department = self.department
        if department:
            domain += [('department', '=', department.id)]
        disease = self.disease
        if disease:
            domain += [('disease', '=', disease.id)]
        op = self.env['hospital.op'].search_read(domain)
        data = {
            'op': op,
            'form_data': self.read()[0]
        }
        return self.env.ref('hospital.report_patient_xlsx').report_action(self, data=data)



