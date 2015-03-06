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


class ix_notification_reset_sequence(orm.TransientModel):
    _name = 'ix.notification.reset.sequence'

    _columns = {
        'new_number': fields.integer('New Next Number', requirde=True),
    }

    def reset(self, cr, uid, ids, context):
        active_ids = context.get('active_ids', [])
        for item in self.browse(cr, uid, ids, context=context):
            self.pool.get('ir.sequence').reset_sequence_ix(cr, uid, active_ids, item.new_number, context=context)
        return {'type': 'ir.actions.act_window_close'}
