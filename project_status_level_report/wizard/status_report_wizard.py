# -*- coding: utf-8 -*-
#############################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2019-TODAY Cybrosys Technologies(<https://www.cybrosys.com>).
#    Author: Cybrosys Techno Solutions(<https://www.cybrosys.com>)
#
#    You can modify it under the terms of the GNU AFFERO
#    GENERAL PUBLIC LICENSE (AGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU AFFERO GENERAL PUBLIC LICENSE (AGPL v3) for more details.
#
#    You should have received a copy of the GNU AFFERO GENERAL PUBLIC LICENSE
#    (AGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################
from odoo import models, fields, api
from odoo.exceptions import UserError


class StatusReportWizard(models.TransientModel):
    _name = 'status.report.wizard'

    date_from = fields.Datetime('Start Date')
    date_to = fields.Datetime('End Date')

    def print_report_xls(self):
        print("in function")
        domain = []
        date_from = self.date_from
        if date_from:
            domain += [('date', '>=', date_from)]
        date_to = self.date_to
        if date_from:
            domain += [('date', '<=', date_to)]
        project_obj = self.env['project.project']
        active_ids = self.env.context.get('active_ids', [])
        if len(active_ids) > 1:
            raise UserError(
                "Warning...! Selection of multiple record is not allowed.")
        else:
            rec = project_obj.browse(active_ids)
            print("record=", rec)
            print("record id=", rec.id)
            data = {
               'form': self.read()[0],
               'record': rec.id
            }
            print("data=", data)
            print("length=", len(active_ids))
            return self.env.ref('project_status_level_report.project_status_report_new').report_action(self,
                                                                           data=data)

