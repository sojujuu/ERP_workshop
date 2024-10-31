# -*- coding: utf-8 -*-
# from odoo import http


# class Workshop1(http.Controller):
#     @http.route('/workshop_1/workshop_1', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/workshop_1/workshop_1/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('workshop_1.listing', {
#             'root': '/workshop_1/workshop_1',
#             'objects': http.request.env['workshop_1.workshop_1'].search([]),
#         })

#     @http.route('/workshop_1/workshop_1/objects/<model("workshop_1.workshop_1"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('workshop_1.object', {
#             'object': obj
#         })

