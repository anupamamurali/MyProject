from odoo import api, fields, models


class PatientReportWizard(models.TransientModel):
    _name = "patient.report.wizard"
    _description = "Patient Report Wizard"

    patient_id = fields.Many2one('hospital.patient.card', string='Patient Id')
    patient_name = fields.Many2one(string='Patient Name',
                                   related='patient_id.patient_name')
    doctor = fields.Many2one('hr.employee',
                             domain="[('job_position','=','Doctor')]")
    department = fields.Many2one(string='Department',
                                 related='doctor.department_id')
    disease = fields.Many2one('hospital.disease', string='Disease')
    from_date = fields.Date(string='From Date')
    to_date = fields.Date(string='To Date')

    def create_patient_report(self):
        print("Test...", self.read()[0])
        data = {
            'form_data': self.read()[0]
        }
        print(data)
        return self.env.ref('hospital.action_report_patient').report_action(self, data=data)



