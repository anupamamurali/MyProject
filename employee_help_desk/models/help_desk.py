from odoo import api, fields, models


class HelpDesk(models.Model):
    _name = "help.desk"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Employee Help Desk"
    _rec_name = 'rec_name'

    emp_name_id = fields.Many2one('res.users', string='Employee', default=lambda self: self.env.user, readonly=True)
    category_id = fields.Many2one('help.category', string='Type Of Ticket', readonly=True)
    company_id = fields.Many2one('res.company', string='Company', default=lambda self: self.env.company, readonly=True)
    state = fields.Selection([('draft', 'Draft'),
                              ('confirm', 'Confirmed'), ('reject', 'Rejected')],
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
