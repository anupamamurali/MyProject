from odoo import api, fields, models
from datetime import datetime


class HospitalOP(models.Model):
    _name = "hospital.op"
    _description = "Hospital OP"

    patient_card = fields.Many2one('hospital.patient.card',
                                   string='Patient Card', required=True)
    name = fields.Char(string='OP Reference', required=True, copy=False,
                       readonly=True, default=lambda self: 'New')
    patient_name = fields.Many2one(string='Patient Name',
                           related='patient_card.patient_name', store=True)
    age = fields.Integer(string='Age', related='patient_card.age')
    gender = fields.Selection(related='patient_card.gender')
    blood_group = fields.Selection(related='patient_card.blood_group')
    date = fields.Date(string='Date', default=datetime.today())
    doctor = fields.Many2one('hr.employee',
                             domain="[('is_doctor','=',True)]")
    department = fields.Many2one(string='Department',
                                 related='doctor.department_id', store=True)
    disease = fields.Many2one('hospital.disease', string='Disease',
                              required=True)
    currency_id = fields.Many2one('res.currency', string='Currency')
    fee = fields.Monetary(string='Fee', related='doctor.fee')
    state = fields.Selection([('draft', 'Draft'), ('op', 'OP')],
                             string='Status', default='draft')
    token = fields.Char(string='Token', readonly=True)

    @api.model
    def create(self, vals):
        """Sequence Generation"""
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code(
                'hospital.op') or 'New'
        res = super(HospitalOP, self).create(vals)
        return res

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
        invoice = self.env['account.move'].create({
           'move_type': 'out_invoice',
           'partner_id': self.patient_name,
           'state': 'draft',
           'invoice_date': datetime.today(),
           'invoice_line_ids': [(0, 0, {
                'name': 'OP',
                'quantity': 1,
                'price_unit': self.fee
           })]
        })
