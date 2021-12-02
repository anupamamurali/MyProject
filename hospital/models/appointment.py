from odoo import fields, models
from datetime import datetime


class HospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Hospital Appointment"

    patient_card = fields.Many2one('hospital.patient.card',
                                   string='Patient Card', required=True)
    name = fields.Many2one(string='Patient Name',
                           related='patient_card.patient_name')
    date = fields.Date(string='Date', default=datetime.today())
    doctor = fields.Many2one('hr.employee',
                             domain="[('is_doctor','=',True)]")
    department = fields.Many2one(string='Department',
                                 related='doctor.department_id')
    state = fields.Selection([('draft', 'Draft'),
                              ('appointment', 'Appointment'), ('op', 'OP')],
                             string='Status', default='draft',
                             track_visibility='always')
    token = fields.Char(string='Token', readonly=True)
    op_count = fields.Integer(string='OP Count', compute='_compute_op_count')

    def _compute_op_count(self):
        count = len(self.env['hospital.op'].search([('patient_card', '=',
                                                     self.patient_card.name)]))
        self.op_count = count

    def action_confirm(self):
        self.state = 'appointment'
        count1 = len(self.env['hospital.op'].search([('date', '=',
                                                     self.date),
                                                    ('doctor', '=',
                                                     self.doctor.name),
                                                    ('state', '=', 'op')]))
        count2 = len(self.env['hospital.appointment'].search([('date', '=',
                                                             self.date),
                                                             ('doctor', '=',
                                                             self.doctor.name),
                                                             ('state', '=',
                                                              'appointment')]))
        self.token = count1 + count2

    def action_op(self):
        self.state = 'op'
        vals = {
            'patient_card': self.patient_card.id,
            'doctor': self.doctor.id,
            'date': self.date,
            'token': self.token,
            'state': 'op'
        }
        self.env['hospital.op'].create(vals)

    def action_open_op(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'OP',
            'res_model': 'hospital.op',
            'domain': [('patient_card', '=', self.patient_card.name)],
            'view_mode': 'tree,form',
            'target': 'current'
        }
