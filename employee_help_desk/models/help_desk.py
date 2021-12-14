from odoo import api, fields, models
from datetime import datetime


class HelpDesk(models.Model):
    _name = "help.desk"
    _inherit = ["mail.thread", "mail.activity.mixin", "portal.mixin"]
    _description = "Employee Help Desk"
    _rec_name = 'rec_name'

    employee_id = fields.Many2one('hr.employee', string='Employee')
    category_id = fields.Many2one('help.category', string='Type Of Ticket')
    created_date = fields.Date(string="Created Date", default=datetime.today())
    company_id = fields.Many2one('res.company', string='Company', default=lambda self: self.env.company, readonly=True)
    state = fields.Selection([('draft', 'Draft'),
                              ('confirm', 'Confirmed'), ('cancel', 'Cancelled')],
                             string='Status', default='draft', tracking=True)
    rec_name = fields.Char(string='Ticket NO', required=True, copy=False,
                           readonly=True, default=lambda self: 'New')

    @api.model
    def create(self, vals):
        """Sequence Generation"""
        if vals.get('rec_name', 'New') == 'New':
            vals['rec_name'] = self.env['ir.sequence'].next_by_code(
                'help.desk') or 'New'
        res = super(HelpDesk, self).create(vals)
        return res

    def action_confirm(self):
        self.state = 'confirm'

    def action_reject(self):
        self.state = 'reject'

    def _compute_access_url(self):
        super(HelpDesk, self)._compute_access_url()
        for order in self:
            order.access_url = '/my/helpdesk/%s' % (order.id)

    def _get_report_base_filename(self):
        self.ensure_one()
        return 'Helpdesk Request-%s' % (self.emp_name)


