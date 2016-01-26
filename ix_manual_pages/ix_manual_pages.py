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
from tools.translate import _


class ix_manual_pages(orm.Model):
    _name = 'ix.manual.pages'
    _description = 'Tutorial'
    _order = 'name'
    _columns = {
        'name': fields.char('Name', required=True),
        'step_ids': fields.one2many('ix.doc.step', 'manual_id', 'Start Tutorial'),
        'description':  fields.text('Description'),
        'categ_id': fields.many2one('ix.manual.categ', 'Category'),
        'user_id': fields.many2one('res.users', 'Author', readonly=True),
    }

    _defaults = {
        'user_id': lambda self, cr, uid, context: uid,
    }

    def start_read_tutorial(self, cr, uid, ids, context=None):
        if context is None:
            context = {}
        for man in self.browse(cr, uid, ids, context=context):
            res = self.pool.get('ix.doc.step').search(cr, uid, [('manual_id', '=', man.id), ('prev_id', '=', False)], context=context)
            if len(res) != 1:
                raise orm.except_orm(_('Error!'), _('The steps isn\'t well configured. Please check if there is only ONE step with Previous field omitted as start point of reading.'))
        view_id = self.pool.get('ir.model.data').get_object(cr, uid, 'ix_manual_pages', 'doc_step_form_view_ix', context=context).id
        return {
            'type': 'ir.actions.act_window',
            'name': _('Read the Tutorial'),
            'view_mode': 'form',
            'view_type': 'form',
            'res_model': 'ix.doc.step',
            'nodestroy': True,
            'target': 'current',
            'context': context,
            'view_id': view_id,
            'res_id': res[0],
        }

    def create_step(self, cr, uid, ids, context=None):
        if context is None:
            context = {}

        for x in self.browse(cr, uid, ids, context=context):
            context['manual_id'] = x.id

        res_id = self.pool.get('create.man.sequence').create(cr, uid, {'manual_id': context.get('manual_id', False)}, context=context)
        view_id = self.pool.get('ir.model.data').get_object(cr, uid, 'ix_manual_pages', 'create_step_form_view', context=context).id

        return {
            'type': 'ir.actions.act_window',
            'name': _('Create new step'),
            'view_mode': 'form',
            'res_model': 'create.man.sequence',
            'target': 'new',
            'context': context,
            'view_id': view_id,
            'res_id': res_id,
        }

    def _sequence_check(self, cr, uid, ids, context=None):
        for man in self.browse(cr, uid, ids, context=context):
            # Set max iteration value as the length of record number
            max_iter = len(man.step_ids)

            # Check whether short or long steps.
            if man.step_ids and max_iter > 1:
                # Should check the head and tail. The sequences has one head and one tail.
                head = [x for x in man.step_ids if not x.prev_id]
                tail = [x for x in man.step_ids if not x.next_id]
                if len(head) != 1 or len(tail) != 1:
                    raise orm.except_orm(_('Error!'), _('Tutorial should have a step with no Previous entry and a step with no Next entry'))

                part = head[0]
                head = True
                tail = False
                length = 1
                for i in range(1, max_iter):
                    length += 1
                    part = part.next_id
                    if head:
                        head = False
                    if part:
                        if not part.next_id:
                            tail = True
                    else:
                        break

                if length != max_iter or not tail:
                        raise orm.except_orm(_('Error!'), _('The steps sequence is not in correct order. Please check the Steps.!'))

            # This section only for a single step
            elif len(man.step_ids) == 1:
                for x in man.step_ids:
                    if x.prev_id or x.next_id:
                        raise orm.except_orm(_('Error!'), _('Tutorial with single step can\'t have previous or next step.'))
        return True

    def create(self, cr, uid, vals, context=None):
        res = super(ix_manual_pages, self).create(cr, uid, vals, context=context)
        self._sequence_check(cr, uid, [res], context=context)
        return res

    def write(self, cr, uid, ids, vals, context=None):
        res = super(ix_manual_pages, self).write(cr, uid, ids, vals, context=context)
        if not isinstance(ids, list):
            ids = [ids]
        self._sequence_check(cr, uid, ids, context=context)
        return res

    def unlink(self, cr, uid, ids, context=None):
        for man in self.browse(cr, uid, ids, context=context):
            for x in man.step_ids:
                x.unlink(context=context)
        return super(ix_manual_pages, self).unlink(cr, uid, ids, context=context)


class ix_manual_categ(orm.Model):
    _name = 'ix.manual.categ'
    _description = 'Tutorial Category'
    _columns = {
        'name': fields.char('Name', required=True),
        'manual_ids': fields.one2many('ix.manual.pages', 'categ_id', 'Tutorials')
    }
