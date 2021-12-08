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
        return request.render('website_maintenance.request_thanks', {})