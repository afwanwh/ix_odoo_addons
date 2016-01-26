# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (c) 2011 - 2015 Vikasa Infinity Anugrah <http://www.infi-nity.com>
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
#    along with this program.  If not, see http://www.gnu.org/licenses/.
#
##############################################################################

from osv import orm, fields


class create_man_sequence(orm.TransientModel):
    _name = 'create.man.sequence'

    def prev_id_default(self, cr, uid, context=None):
        res = False
        manual_id = context.get('manual_id', False)
        if manual_id:
            for seq in self.pool.get('ix.manual.pages').browse(cr, uid, manual_id, context=context).step_ids:
                if not seq.next_id:
                    res = seq.id
        return res

    _columns = {
        'prev_id': fields.many2one('ix.doc.step', 'After'),
        'next_id': fields.many2one('ix.doc.step', 'Before'),
        'manual_id': fields.many2one('ix.manual.pages', 'Tutorial', readonly=True),
        'name': fields.char('Name'),
        'content':  fields.text('Content'),
    }

    _defaults = {
        'prev_id': prev_id_default,
    }

    def onchange_next(self, cr, uid, ids, next_id, prev_id, context=None):
        val = {}
        seq_obj = self.pool.get('ix.doc.step')
        if next_id:
            parent = seq_obj.browse(cr, uid, next_id, context=context).prev_id and seq_obj.browse(cr, uid, next_id, context=context).prev_id.id or False
            if parent:
                val['value'] = {'prev_id': parent}
            else:
                val['value'] = {'prev_id': False}
        elif not next_id and prev_id and seq_obj.browse(cr, uid, prev_id, context=context).next_id:
            val['value'] = {'prev_id': False}
        return val

    def onchange_prev(self, cr, uid, ids, next_id, prev_id, context=None):
        val = {}
        seq_obj = self.pool.get('ix.doc.step')
        if prev_id:
            child = seq_obj.browse(cr, uid, prev_id, context=context).next_id and seq_obj.browse(cr, uid, prev_id, context=context).next_id.id or False
            if child:
                val['value'] = {'next_id': child}
            else:
                val['value'] = {'next_id': False}
        elif not prev_id and next_id and seq_obj.browse(cr, uid, next_id, context=context).prev_id:
            val['value'] = {'next_id': False}
        return val

    def _create_step(self, cr, uid, ids, context=None):
        for obj in self.browse(cr, uid, ids, context=context):
            manual_id = context.get('active_id', False)

            step_obj = self.pool.get('ix.doc.step')
            prev_id = []
            next_id = []
            if obj.prev_id:
                prev_id = obj.prev_id.id
            if obj.next_id:
                next_id = obj.next_id.id

            vals = {
                'name': obj.name,
                'manual_id': manual_id,
                'prev_id': prev_id,
                'next_id': next_id,
                'content': obj.content,
            }

            step_id = step_obj.create(cr, uid, vals, context=context)
            if prev_id:
                obj.prev_id.write({'next_id': step_id}, context=context)
            if next_id:
                obj.prev_id.write({'prev_id': step_id}, context=context)
        return step_id

    def create_step(self, cr, uid, ids, context=None):
        self._create_step(cr, uid, ids, context=context)
        return {'type': 'ir.actions.act_window_close'}
