from odoo import http
from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale




class LMS(http.Controller):

    @http.route('/member_webform', type="http", auth="public", website=True)
    def member_webform(self, **kw):
        return http.request.render('lms.create_member', {'member_name': 'Tushi'})

    @http.route('/create/webmember', type="http", auth="public", website=True)
    def create_webmember(self, **kw):
        request.env['lms.members'].sudo().create(kw)
        return request.render("lms.member_thanks", {})

 # Sample Controller Created
    @http.route('/books', website=True, auth='user')
    def lms_books(self, **kw):
        books = request.env['lms.books'].sudo().search([])
        return request.render("lms.books_page", {
            'books': books
        })
    # for home page
    @http.route('/lmsbooks', website=True, auth='user')
    def lms_home_books(self, **kw):
        books = request.env['lms.books'].sudo().search([])
        return request.render("lms.home_books_page", {
            'books': books
        })

    @http.route('/get_books', type='http', auth='public')
    def get_books(self):
        print("Yes here entered")
        books_rec = request.env['lms.books'].search([])
        books = []
        for rec in books_rec:
            vals = {
                'name': rec.book_name,
            }
            books.append(vals)
        print("Books List--->", books)
        data = {'status': 200, 'response': books, 'message': 'Done All books Returned'}
        return data

    # @http.route(['/cms/report/print'], type='http', auth="public", website=True)
    # def print_books(self, **kw):
    #     cr, uid, context = request.cr, SUPERUSER_ID, request.context
    #     if 2:
    #         pdf = request.registry['report'].get_pdf(cr, uid, [2], 'x.cms_html_body', data=None,
    #                                                 context=context)
    #         pdfhttpheaders = [('Content-Type', 'application/pdf'), ('Content-Length', len(pdf))]
    #         return request.make_response(pdf, headers=pdfhttpheaders)

    @http.route(['/books/print'], type='http', auth="public", website=True)
    def print_books(self, **kwargs):
        books = request.env['lms.books'].sudo().search([])
        # books_id = request.session.get('books_id')
        if books:
            pdf = request.env.ref('lms.report_books').sudo().report_action([self.id])[0]
            # pdf = request.env.ref('lms.report_books').sudo()._render_qweb_pdf([self.id])[0]
            # pdf = self.env.ref('lms.report_books')._render_qweb_pdf(self.id)[0]
            # pdf, _ = request.env.ref('lms.report_books').sudo().render_qweb_pdf([books])
            pdfhttpheaders = [('Content-Type', 'application/pdf'), ('Content-Length', len(pdf))]
            return request.make_response(pdf, headers=pdfhttpheaders)
        else:
            return request.redirect('/books')




class WebsiteSaleInherit(WebsiteSale):

    @http.route([
        '''/shop''',
        '''/shop/page/<int:page>''',
        '''/shop/category/<model("product.public.category", "[('website_id', 'in', (False, current_website_id))]"):category>''',
        '''/shop/category/<model("product.public.category", "[('website_id', 'in', (False, current_website_id))]"):category>/page/<int:page>'''
    ], type='http', auth="public", website=True)
    def shop(self, page=0, category=None, search='', ppg=False, **post):
        res = super(WebsiteSaleInherit, self).shop(page=0, category=None, search='', ppg=False, **post)
        print("Inherited Odoo Mates ....", res)
        return res