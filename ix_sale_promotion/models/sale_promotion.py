# -*- coding: utf-8 -*-
##############################################################################
#
#    Afwan Wali Hamim
#    Copyright (C) 2015 Afwan Wali Hamim <afwanwalihamim@gmail.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp import api, fields, models, _


class sale_promotion(models.Model):
    _name = 'sale.promotion'

    name = fields.Char(string='Title', required=True, help='Title of promotion.')
    code = fields.Char(string='Code', required=True, help='Code of promotion. Must be unique!')
    type = fields.Selection([('fixed', 'Fixed Amount Discount'), ('free', 'Buy X Free Y'), ('percentage', 'Percentage Discount')], string='Promotion Type', required=True, default='fixed')
    amount_discount = fields.Float(string='Amount of Disc')
    percentage_discount = fields.Float(string='Discount Percentage')
    point_values = fields.Float(string='Value of a Point')
    state = fields.Selection([('off', 'Inactive'), ('on', 'Active')], string='Status', default='off')
    buy_qty = fields.Integer(string='Buy Qty')
    free_qty = fields.Integer(string='Free Qty')
    usage = fields.Selection([('product', 'Product Only'), ('subtotal', 'Subtotal in Sale Order'), ('total', 'Total in Sale Order')], string='Apply for')
    points_categ = fields.Selection([('product', 'Point from Products'), ('sale', 'Point from Total Sale')], string='Point Category')

    _sql_constraints = [('code_uniq', 'UNIQUE(code)', _('Two or more same codes are disallowed. Define another code.'))]

    @api.multi
    def turn_promotion_on(self):
        return self.write({'state': 'on'})

    @api.multi
    def turn_promotion_off(self, cr, uid, ids, context=None):
        return self.write({'state': 'off'})
