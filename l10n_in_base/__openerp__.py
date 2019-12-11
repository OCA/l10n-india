# -*- coding: utf-8 -*-
###########################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) OpenERP SA (<http://openerp.com).
#    Copyright (C) 2011-Today Serpent Consulting Services Pvt. Ltd.
#    (<http://www.serpentcs.com>)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>
#
##########################################################################

{
    'name': 'Indian Localization',
    'version': '8.0.1.0.0',
    'author': 'OpenERP SA, Odoo Community Association (OCA),\
               Serpent Consulting Services Pvt. Ltd.',
    'website': 'https://www.serpentcs.com',
    'category': 'Indian Localization',
    'summary': 'Indian Localization Base',
    'depends': ['base'],
    'data': [
        'security/l10n_in_base_groups.xml',
        'views/res_config_view.xml',
    ],
    'installable': True,
    'application': False,
}
