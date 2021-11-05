from odoo import api, fields, models
from datetime import datetime


class HospitalOP(models.Model):
    _name = "hospital.op"
    _description = "Hospital OP"

    patient_card = fields.Many2one('hospital.patient.card',
                                   string='Patient Card', required=True)
    name = fields.Many2one(string='Patient Name',
                           related='patient_card.patient_name')
    age = fields.Integer(string='Age', related='patient_card.age')
    gender = fields.Selection(related='patient_card.gender')
    blood_group = fields.Selection(related='patient_card.blood_group')
    date = fields.Date(string='Date', default=datetime.today())
    doctor = fields.Many2one('hr.employee',
                             domain="[('job_position','=','Doctor')]")
    department = fields.Many2one(string='Department',
                                 related='doctor.department_id')
    currency_id = fields.Many2one('res.currency', string='Currency')
    # fee = fields.Monetary(string='Fee')
    fee = fields.Monetary(string='Fee', related='doctor.fee')
    state = fields.Selection([('draft', 'Draft'), ('op', 'OP')],
                             string='Status', default='draft')
    token = fields.Char(string='Token', readonly=True)
   # products = fields.Many2many('product.product', domain="[('product_tmpl_id.type', '=', ""'service')]")

    def action_confirm(self):
        self.state = 'op'
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

    def action_create_invoice(self):
        data = [0, 0, {
            'name': 'OP',
            'quantity': 1,
            'price_unit': self.fee
        }]
        invoice = self.env['account.move'].create({
            'move_type': 'out_invoice',
            'ref': self.patient_card.id,
            'partner_id': self.name,
            'state': 'draft',
            'invoice_date': datetime.today(),
            'date': datetime.today(),
            'invoice_line_ids': data
        })

