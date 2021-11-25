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
        args = {
            'patient_card': self.patient_card.id,
            'date_from': self.date_from,
            'date_to': self.date_to,
            'doctor': self.doctor.id,
            'disease': self.disease.id
        }
        self.env.cr.execute("""SELECT o.name as op,
                                      r.display_name as patient_name,
                                      o.date as date,
                                      e.name as doctor,
                                      de.name as department,
                                      d.name as disease FROM hospital_op o
        LEFT OUTER JOIN hospital_patient_card p ON(o.patient_card=p.id)
        LEFT OUTER JOIN res_partner r ON(o.patient_name=r.id)
        LEFT OUTER JOIN hr_employee e ON(o.doctor=e.id)
        LEFT OUTER JOIN hr_department de ON(o.department=de.id)
        LEFT OUTER JOIN hospital_disease d ON(o.disease=d.id)
        WHERE (o.patient_card = %(patient_card)s AND o.date BETWEEN
        %(date_from)s AND %(date_to)s AND o.doctor = %(doctor)s AND
        o.disease = %(disease)s )""", args)
        result = self.env.cr.dictfetchall()
        print(result)
        data = {
            'form_data': self.read()[0],
            'op': result
        }
        return self.env.ref('hospital.action_report_patient').report_action(
            self, data=data)

    def create_patient_excel_report(self):
        args = {
            'patient_card': self.patient_card.id,
            'date_from': self.date_from,
            'date_to': self.date_to,
            'doctor': self.doctor.id,
            'disease': self.disease.id
        }
        self.env.cr.execute("""SELECT o.name as op,
                                      r.display_name as patient_name,
                                      o.date as date,
                                      e.name as doctor,
                                      de.name as department,
                                      d.name as disease FROM hospital_op o
                LEFT OUTER JOIN hospital_patient_card p ON(o.patient_card=p.id)
                LEFT OUTER JOIN res_partner r ON(o.patient_name=r.id)
                LEFT OUTER JOIN hr_employee e ON(o.doctor=e.id)
                LEFT OUTER JOIN hr_department de ON(o.department=de.id)
                LEFT OUTER JOIN hospital_disease d ON(o.disease=d.id)
                WHERE (o.patient_card = %(patient_card)s AND o.date BETWEEN
                %(date_from)s AND %(date_to)s AND o.doctor = %(doctor)s AND
                o.disease = %(disease)s )""", args)
        result = self.env.cr.dictfetchall()
        data = {
            'form_data': self.read()[0],
            'op': result
        }
        return self.env.ref('hospital.report_patient_xlsx').report_action(self, data=data)
