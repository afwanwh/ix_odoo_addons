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
    'name': 'Enchancement of Document Page by iXotem',
    'version': '0.1',
    'category': 'Knowledge Management',
    'sequence': 1,
    'summary': 'Step by step self help.',
    'description': """
        Provide step-by-step help which is integrated inside document page module.
        You could make tutorial of using odoo or anything else with this module.
    """,
    'author': 'Afwan Wali Hamim',
    'website': 'http://ixotem.blogspot.com/',
    'depends': ['knowledge'],
    'data': [
        'security/ir.model.access.csv',
        'ix_manual_pages_view.xml',
        'ix_doc_step_view.xml',
    ],
    'demo': [],
    'test': [
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
