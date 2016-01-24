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

from openerp.osv import orm, fields


class ix_manual_pages(orm.Model):
    _name = 'ix.manual.pages'
    _description = 'Tutorial'
    _order = 'name'
    _columns = {
        'name': fields.char('Name', required=True),
        'next_id': fields.many2one('ix.doc.step', 'Start Tutorial'),
        'description':  fields.text('Description'),
        'categ_id': fields.many2one('ix.manual.categ', 'Category'),
    }


class ix_manual_categ(orm.Model):
    _name = 'ix.manual.categ'
    _description = 'Tutorial Category'
    _columns = {
        'name': fields.char('Name', required=True),
        'manual_ids': fields.one2many('ix.manual.pages', 'categ_id', 'Tutorials')
    }
