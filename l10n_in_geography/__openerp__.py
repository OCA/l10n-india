# -*- coding: utf-8 -*-
###########################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2012-Today Serpent Consulting Services Pvt. Ltd.
#    (<http://www.serpentcs.com>)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>
#
############################################################################
{
    'name': 'Indian Geography',
    'version': '1.0',
    'category': 'Indian Localization',
    'summary': 'List of States and Cities in India',
    'description': """
List of States and Cities in India
==================================
This module adds all the major cities of India by state.

In order to work with Indian Localization, these module eases the effort
to manually add cities and states of India.
This module was developed by Serpent Consulting Services Pvt. Ltd.
    Not covered under Odoo Maintenance Contract or Business Pack.
    Contact at contact@serpentcs.com if you are looking for
    support or customization.
""",
    'author': 'OpenERP SA',
    'website': 'http://www.openerp.com',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'data/res_country_state_data.xml',
        'data/res_city_data.xml',
        'res_city_view.xml',
        'res_partner_view.xml'
    ],
    'installable': True,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
