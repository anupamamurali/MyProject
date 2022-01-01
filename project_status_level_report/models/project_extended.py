from odoo import models, fields


class ProjectExtended(models.Model):
    _inherit = 'project.project'

    planned_amount = fields.Float('Initially Planned Amount', help='Estimated cost to do the task.')
