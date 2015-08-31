# -*- coding: utf-8 -*-
###########################################################################
#
#    OpenERP, Open Source Management Solution
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
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>
#
############################################################################
{
    'name': 'Annexure 2A/2B',
    'version': '1.0',
    'author': 'Serpent Consulting Services Pvt. Ltd.',
    'website': 'https://www.serpentcs.com',
    'sequence': 120,
    'category': 'Indian Localization',
    'summary': 'Annexure 2A/2B',
    'description': """This modules does
Annexure 2A is the Summary of DVAT-30 (Purchases),
and Annexure 2B is the Summary of DVAT-31 (Sales).


""",
    'depends': ['l10n_in_base', 'l10n_in_account_tax', 'sale', 'purchase'],
    'data': [
        'report/annexure_2a_report_view.xml',
        'report/annexure_2b_report_view.xml',
    ],
    'installable': True,
    'application': True,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
