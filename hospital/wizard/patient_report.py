from odoo import api, fields, models


class PatientReportWizard(models.TransientModel):
    _name = "patient.report.wizard"
    _description = "Patient Report Wizard"

    patient_card_id = fields.Many2one('hospital.patient.card', string='Patient Id')
    patient_name_id = fields.Many2one(string='Patient Name',
                                   related='patient_card_id.patient_name')
    doctor_id = fields.Many2one('hr.employee',
                             domain="[('job_position','=','Doctor')]")
    department_id = fields.Many2one(string='Department',
                                 related='doctor_id.department_id')
    disease_id = fields.Many2one('hospital.disease', string='Disease')
    date_from = fields.Date(string='From Date')
    date_to = fields.Date(string='To Date')

    def create_patient_report(self):
        if self.patient_card_id and self.date_from and self.date_to and self.doctor_id and self.disease_id:
            args = {
            'patient_card': self.patient_card_id.id,
            'date_from': self.date_from,
            'date_to': self.date_to,
            'doctor': self.doctor_id.id,
            'disease': self.disease_id.id
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
        elif self.patient_card_id and self.date_from and self.date_to and self.doctor_id:
            args = {
            'patient_card': self.patient_card_id.id,
            'date_from': self.date_from,
            'date_to': self.date_to,
            'doctor': self.doctor_id.id,
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
            %(date_from)s AND %(date_to)s AND o.doctor = %(doctor)s)""", args)
        elif self.patient_card_id and self.date_from and self.date_to:
            args = {
            'patient_card': self.patient_card_id.id,
            'date_from': self.date_from,
            'date_to': self.date_to
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
            %(date_from)s AND %(date_to)s)""", args)
        elif self.patient_card_id:
            args = {
            'patient_card': self.patient_card_id.id
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
            WHERE (o.patient_card = %(patient_card)s)""", args)
        else:
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
                       LEFT OUTER JOIN hospital_disease d ON(o.disease=d.id)""")

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
            'patient_card': self.patient_card_id.id,
            'date_from': self.date_from,
            'date_to': self.date_to,
            'doctor': self.doctor_id.id,
            'disease': self.disease_id.id
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
