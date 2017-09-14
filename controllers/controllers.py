# -*- coding: utf-8 -*-
from openerp import http

# class L10nArCtaCte(http.Controller):
#     @http.route('/l10n_ar_cta_cte/l10n_ar_cta_cte/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/l10n_ar_cta_cte/l10n_ar_cta_cte/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('l10n_ar_cta_cte.listing', {
#             'root': '/l10n_ar_cta_cte/l10n_ar_cta_cte',
#             'objects': http.request.env['l10n_ar_cta_cte.l10n_ar_cta_cte'].search([]),
#         })

#     @http.route('/l10n_ar_cta_cte/l10n_ar_cta_cte/objects/<model("l10n_ar_cta_cte.l10n_ar_cta_cte"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('l10n_ar_cta_cte.object', {
#             'object': obj
#         })