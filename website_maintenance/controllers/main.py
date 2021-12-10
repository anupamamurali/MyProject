from odoo import http
from odoo.http import request


class MaintenanceRequest(http.Controller):

    @http.route('/maintenance_webform', type="http", auth="public", website=True)
    def maintenance_webform(self, **kwargs):
        print("in function")
        maintenance_teams = request.env['maintenance.team'].sudo().search([])
        return http.request.render('website_maintenance.create_request',
                                   {'name': kwargs.get('name'),
                                    'customer_name': kwargs.get('customer_name'),
                                    'email_cc': kwargs.get('email_cc'),
                                    'maintenance_teams': maintenance_teams})

    @http.route('/create/maintenancerequest', type="http", auth="public", website=True)
    def create_maintenancerequest(self, **kwargs):
        print("Data Received:", kwargs)
        name = kwargs.get('name')
        customer_name = kwargs.get('customer_name')
        maintenance_team_id = int(kwargs.get('maintenance_team_id'))
        email_cc = kwargs.get('email_cc')
        values = {
            'name': name,
            'customer_name': customer_name,
            'email_cc': email_cc,
            'maintenance_team_id': maintenance_team_id
            }
        req_id = request.env['maintenance.request'].sudo().create(values)
        print("ghjk")
        user_id = request.env.user.id
        template = request.env.ref('website_maintenance.request_email_template',
                                   raise_if_not_found=False)
        if template:
            template.sudo().send_mail(req_id.id, force_send=True)
        # self.env.ref('website_maintenance.request_email_template').send_mail(
        #     self.id, force_send=True)
        return request.render('website_maintenance.request_thanks', {})
