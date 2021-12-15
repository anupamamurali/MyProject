from odoo import http
from odoo.http import request
import base64
from collections import OrderedDict
from odoo.exceptions import AccessError, MissingError
from odoo.http import request, Response
from odoo.tools import image_process
from odoo.tools.translate import _
from odoo.addons.portal.controllers.portal import pager as portal_pager, \
    CustomerPortal
from odoo.addons.web.controllers.main import Binary


class HelpdeskRequest(http.Controller):

    @http.route('/helpdesk_webform', type="http", auth="public", website=True)
    def helpdesk_webform(self, **kwargs):
        print("in function")
        employees = request.env['hr.employee'].sudo().search([])
        emp_id = request.env.user.employee_id
        print("employee:", emp_id)
        categories = request.env['help.category'].sudo().search([])
        return http.request.render(
            'employee_help_desk.create_ticket', {'emp_id': emp_id,
                                                 'employees': employees,
                                                 'categories': categories,
                                                 'subject': kwargs.get('subject')})

    @http.route('/create/helpdeskticket', type="http", auth="public", website=True)
    def create_helpdeskticket(self, **kwargs):
        print("Data Received:", kwargs)
        print("employees:", kwargs.get('employees'))
        values = {
            'employee_id': kwargs.get('employee_id'),
            'category_id': kwargs.get('category_id'),
            'subject': kwargs.get('subject')
            }
        request.env['help.desk'].sudo().create(values)
        return request.render('employee_help_desk.ticket_thanks', {})


class CustomerPortal(CustomerPortal):

    def _prepare_home_portal_values(self, counters):
        values = super()._prepare_home_portal_values(counters)
        if 'helpdesk_count' in counters:
            values['helpdesk_count'] = request.env['help.desk'].search_count([])
        return values

    def _helpdesk_request_get_page_view_values(self, order, access_token,
                                                  **kwargs):
        def resize_to_48(b64source):
            if not b64source:
                b64source = base64.b64encode(Binary.placeholder())
            return image_process(b64source, size=(48, 48))
        values = {
            'order': order,
            'resize_to_48': resize_to_48,
        }
        return self._get_page_view_values(order, access_token, values,
                                          'my_helpdesk_history', False,
                                          **kwargs)

    @http.route(['/my/helpdesk', '/my/helpdesk/page/<int:page>'],
                type='http', auth="user", website=True)
    def portal_my_helpdesk_requests(self, page=1, date_begin=None,
                                       date_end=None, sortby=None,
                                       filterby=None, **kw):
        values = self._prepare_portal_layout_values()
        Helpdesk = request.env['help.desk']
        domain = []

        if date_begin and date_end:
            domain += [('create_date', '>', date_begin),
                       ('create_date', '<=', date_end)]

        searchbar_sortings = {
            'date': {'label': _('Newest'),
                     'order': 'create_date desc, id desc'},
            'rec_name': {'label': _('Ticket NO'), 'order': 'rec_name asc, id asc'},
            'created_date': {'label': _('Created Date'),
                                   'order': 'created_date desc, id desc'},
            'state': {'label': _('State'), 'order': 'state asc, id asc'}
        }
        # default sort by value
        if not sortby:
            sortby = 'rec_name'
        order = searchbar_sortings[sortby]['order']
        searchbar_filters = {
            'all': {'label': _('All'), 'domain': [
                ('state', 'in', ['draft', 'confirm', 'cancel'])]},
            'draft': {'label': _('Draft'), 'domain': [('state', '=', 'draft')]},
            'confirmed': {'label': _('Confirmed'),
                          'domain': [('state', '=', 'confirm')]},
            'cancel': {'label': _('Cancelled'),
                       'domain': [('state', '=', 'cancel')]}
        }
        # default filter by value
        if not filterby:
            filterby = 'all'
        domain += searchbar_filters[filterby]['domain']
        help_count = Helpdesk.search_count(domain)
        pager = portal_pager(
            url="/my/helpdesk",
            url_args={'date_begin': date_begin, 'date_end': date_end,
                      'sortby': sortby, 'filterby': filterby},
            total=help_count,
            page=page,
            step=self._items_per_page
        )
        orders = Helpdesk.search(
            domain,
            order=order,
            limit=self._items_per_page,
            offset=pager['offset']
        )
        request.session['my_helpdesk_history'] = orders.ids[:100]
        values.update({
            'date': date_begin,
            'orders': orders,
            'page_name': 'helpdesk',
            'pager': pager,
            'searchbar_sortings': searchbar_sortings,
            'sortby': sortby,
            'searchbar_filters': OrderedDict(sorted(searchbar_filters.items())),
            'filterby': filterby,
            'default_url': '/my/helpdesk',
        })
        return request.render(
            "employee_help_desk.portal_my_helpdesk_requests", values)

    @http.route(['/my/helpdesk/<int:order_id>'], type='http', auth="public",
                website=True)
    def portal_my_help_request(self, order_id=None, access_token=None, **kw):
        try:
            order_sudo = self._document_check_access('help.desk', order_id,
                                                     access_token=access_token)
        except (AccessError, MissingError):
            return request.redirect('/my')

        report_type = kw.get('report_type')
        if report_type in ('html', 'pdf', 'text'):
            return self._show_report(model=order_sudo, report_type=report_type,
                                     report_ref='employee_help_desk.report_helpdesk_details',
                                     download=kw.get('download'))

        confirm_type = kw.get('confirm')
        if confirm_type == 'reminder':
            order_sudo.confirm_reminder_mail(kw.get('confirmed_date'))
        if confirm_type == 'reception': order_sudo._confirm_reception_mail()
        values = self._helpdesk_request_get_page_view_values(order_sudo,
                                                                access_token,
                                                                **kw)
        if order_sudo.company_id:
            values['res_company'] = order_sudo.company_id
            values['page_name'] = 'helpdesk'
        return request.render(
            "employee_help_desk.portal_my_helpdesk_request", values)

