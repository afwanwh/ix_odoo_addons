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

{
    'name': 'Sequence Manual Reset',
    'version': '0.1',
    'category': 'Tools',
    'sequence': 10,
    'summary': 'Reset sequence manually.',
    'description': """
        This module add Reset button to rewrite Next Number field in sequence view.
        Be careful, some fields cannot has two or more same name due to constraint.
        Check first the field which the sequence will be resetted.
    """,
    'author': 'Afwan Wali Hamim',
    'website': 'http://ixotem.blogspot.com/',
    'depends': ['base'],
    'data': [
        'ir_sequence_view.xml',
        'wizard/notification_view.xml',
    ],
    'demo': [],
    'test': [
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
