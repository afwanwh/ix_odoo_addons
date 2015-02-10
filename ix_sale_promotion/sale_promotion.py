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

from openerp.osv import fields, orm


class sale_promotion(orm.Model):
    _name = 'sale.promotion'

    _columns = {
        'name': fields.char('Tittle', required=True, help='Tittle of promotion.'),
        'code': fields.char('Code', required=True, help='Code of promotion. Must be unique!'),
        'type': fields.selection([('fixed', 'Fixed Amount Discount'), ('free', 'Buy X free Y'), ('percentage', 'Percentage Discount'), ('python', 'Pythonic Formula'), ('points', 'Points Based Discount')], 'Promotion Type', required=True),
        'amount_discount': fields.float('Amount of Disc'),
        'percentage_discount': fields.float('Discount Percentage'),
        'point_values': fields.float('Value of a Point'),
        'python_formula': fields.text('Python Formula'),
        'state': fields.selection([('off', 'OFF'), ('on', 'ON')], 'Status'),
    }

    _defaults = {
        'state': 'off',
    }

    _sql_constraints = [('code_uniq', 'unique(code)', 'Two or more same codes are disallowed. Define another code.')]

    def turn_promotion_on(self, cr, uid, ids, context=None):
        if context is None:
            context = {}
        return self.write(cr, uid, ids, {'state': 'on'}, context=context)

    def turn_promotion_off(self, cr, uid, ids, context=None):
        if context is None:
            context = {}
        return self.write(cr, uid, ids, {'state': 'off'}, context=context)
