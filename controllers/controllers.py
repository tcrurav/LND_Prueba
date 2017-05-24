# -*- coding: utf-8 -*-
from odoo import http

# class Discotecas(http.Controller):
#     @http.route('/discotecas/discotecas/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/discotecas/discotecas/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('discotecas.listing', {
#             'root': '/discotecas/discotecas',
#             'objects': http.request.env['discotecas.discotecas'].search([]),
#         })

#     @http.route('/discotecas/discotecas/objects/<model("discotecas.discotecas"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('discotecas.object', {
#             'object': obj
#         })