from odoo import http
from odoo.http import request


class MaintenanceRequest(http.Controller):

    @http.route('/maintenance_webform', type="http", auth="public", website=True)
    def maintenance_webform(self, **kwargs):
        print("in function")
        return http.request.render('website_maintenance.create_request', {})

    @http.route('/create/maintenancerequest', type="http", auth="public", website=True)
    def create_maintenancerequest(self, **kwargs):
        print("Data Received:", kwargs)
        if kwargs.get('name'):
            name = kwargs.get('name')
            if kwargs.get('maintenance_team_id'):
                maintenance_team_id = int(kwargs.get('maintenance_team_id'))
                email_cc = int(kwargs.get('email'))
                values = {
                    'name': name,
                    'email_cc': email_cc,
                    'maintenance_team_id': maintenance_team_id
                }
                request.env['maintenance.request'].sudo().create(values)
                return request.redirect('maintenance_webform?submitted=1')
        return request.render('website_maintenance.request_thanks', {
            'maintenance_teams': request.env['maintenance.team'].search([]),
            'submitted':kwargs.get('submitted', False)
        })

    def action_email(self):
        print("ghjk")
        self.env.ref('website_maintenance.request_email_template').send_mail(self.id, force_send=True)