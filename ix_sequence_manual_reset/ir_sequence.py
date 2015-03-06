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

from openerp.tools.translate import _
from openerp.osv import orm


class ir_sequence(orm.Model):
    _inherit = 'ir.sequence'

    def reset_sequence_ix(self, cr, uid, ids, new_number, context=None):
        for sequence in self.browse(cr, uid, ids, context=context):
            sequence.write({'number_next_actual': new_number}, context=context)
        return True

    def show_notif(self, cr, uid, ids, context=None):
        if context is None:
            context = {}
        view_id = self.pool.get('ir.model.data').get_object(cr, uid, 'ix_sequence_manual_reset', 'view_notification_reset_sequence_ix', context=context).id
        return {
            'type': 'ir.actions.act_window',
            'name': _('Warning!'),
            'view_mode': 'form',
            'view_type': 'form',
            'view_id': view_id,
            'res_model': 'ix.notification.reset.sequence',
            'nodestroy': True,
            'target': 'new',
            'context': context,
        }
