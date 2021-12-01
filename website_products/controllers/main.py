from odoo import http
from odoo.http import request, route
from odoo.addons.website_sale.controllers.main import WebsiteSale
from werkzeug.exceptions import Forbidden, NotFound


class WebsiteSaleInherit(WebsiteSale):
    @http.route([
        '''/shop''',
        '''/shop/page/<int:page>''',
        '''/shop/category/<model("product.public.category"):category>''',
        '''/shop/category/<model("product.public.category"):category>/page/<int:page>'''
    ], type='http', auth="public", website=True)
    def shop(self, page=0, category=None, search='', ppg=False, **post):
        print("Inherited Odoo")
        user_id = request.uid + 1
        print(user_id)
        user_rec = request.env['res.partner'].search([('id', '=', user_id)])
        category_id = []
        for rec in user_rec:
            category_id += rec.pro_cat_ids
        print(category_id)
        products = user_rec.product_ids
        Category = request.env['product.public.category'].search([('id', '=', category_id)])
       # category = Category.search([('id', 'in', category_id())])
        print(Category)
       # print(category)
        # values = {
        #     'category': categories,
        #     'products': products
        # }
        res = super(WebsiteSaleInherit, self).shop(page=0, category=None, search='', ppg=False, **post)
        return res
