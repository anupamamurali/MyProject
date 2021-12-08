from odoo import api, fields, models
from datetime import date, datetime
from dateutil.relativedelta import relativedelta


class HospitalPatientCard(models.Model):
    _name = "hospital.patient.card"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Hospital Patient Card"

    patient_name = fields.Many2one('res.partner', string='Patient Name',
                                   required=True)
    name = fields.Char(string='Patient Reference', required=True, copy=False,
                       readonly=True, default=lambda self: 'New')
    dob = fields.Date(string='DOB', related='patient_name.dob', store=True)
    age = fields.Integer(string='Age', compute="_compute_birth_date")
    gender = fields.Selection(related='patient_name.gender')
    mobile = fields.Char(related='patient_name.mobile')
    phone = fields.Char(related='patient_name.phone')
    blood_group = fields.Selection([
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
    ])
    op_ids = fields.One2many('hospital.op', 'patient_card',
                             string='OP History')

    @api.model
    def create(self, vals):
        """Sequence Generation"""
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code(
                'hospital.patient.card') or 'New'
        res = super(HospitalPatientCard, self).create(vals)
        return res

    @api.depends('dob')
    def _compute_birth_date(self):
        """Updates age field when birth_date is changed"""
        self.age = False
        if self.dob:
            dob = str(self.dob)
            d1 = datetime.strptime(dob, '%Y-%m-%d')
            d2 = date.today()
            self.age = relativedelta(d2, d1).years
