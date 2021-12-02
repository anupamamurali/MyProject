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
        res = super(WebsiteSaleInherit, self).shop(page=0, category=None,
                                                   search='', ppg=False,
                                                   **post, )
        print("Inherited Odoo")
        user_id = request.env.user
        Category = request.env['product.public.category']
        Product = request.env['product.template'].with_context(bin_size=True)
        print(Category)
        print(Product)
        print(user_id.partner_id)
        user_rec = request.env['res.partner'].search([('id', '=', user_id.partner_id.id)])
        values = {}
        category_id = []
        product_id = []
        if user_rec.pro_cat_ids:
            for rec in user_rec.pro_cat_ids:
                category_id.append(rec.id)
            category = Category.search([('id', 'in', category_id)])
            print(category)
        else:
            category = Category
        values.update({'category': category})
        print("values=", values)
        if user_rec.product_ids:
            for rec in user_rec.product_ids:
                product_id.append(rec.id)
            product = Product.search([('id', 'in', product_id)])
            print(product)
        else:
            product = Product
        values.update({'category': category, 'product': product})
        print("values=", values)
        if category:
            values['main_object'] = category, product
        print(values)
        var = res.qcontext.get('products')
        var = product
        print("var=", var)
        print(res.qcontext.update({'products': product}))
        return res
