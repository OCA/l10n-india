# -*- coding: utf-8 -*-
############################################################################
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
    'name': 'Packing Cost on Invoice',
    'version': '1.0',
    'category': 'Indian Localization',
    'summary': 'Packing Cost on Invoice',
    'description': """
Packing Cost on Invoice
=========================================================================
This module allows you to manage packing cost of the products on invoices.

When the product is packed in a container, you can take into account
the cost of the container in the invoice.

""",
    'author': 'OpenERP SA',
    'website': 'http://www.openerp.com',
    'depends': ['l10n_in_base', 'product_container', 'account'],
    'data': [
        'l10n_in_packing_invoice.xml'
    ],
    'installable': True,
    'auto_install': False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
