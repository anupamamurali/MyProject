from odoo import http
from odoo.http import request


class HelpdeskRequest(http.Controller):

    @http.route('/helpdesk_webform', type="http", auth="public", website=True)
    def helpdesk_webform(self, **kwargs):
        print("in function")
        employees = request.env['res.users'].sudo().search([])
        categories = request.env['help.category'].sudo().search([])
        return http.request.render('employee_help_desk.create_ticket', {
                                                         'employees': employees,
                                                         'categories': categories})

    @http.route('/create/helpdeskticket', type="http", auth="public", website=True)
    def create_helpdeskticket(self, **kwargs):
        print("Data Received:", kwargs)
        values = {
            'emp_name_id': kwargs.get('emp_name_id'),
            'category_id': kwargs.get('category_id')
            }
        request.env['help.desk'].sudo().create(values)
        print("ghjk")
        return request.render('employee_help_desk.ticket_thanks', {})
