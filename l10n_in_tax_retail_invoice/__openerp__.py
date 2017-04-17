# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2011-Today Serpent Consulting Services Pvt. Ltd. (<http://www.serpentcs.com>)
#    Copyright (C) 2004 OpenERP SA (<http://www.openerp.com>)
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
##############################################################################

{
    'name': 'Tax / Retail Invoice',
    'version': '1.0',
    'category': 'Indian Localization',
    'summary':'Print Tax / Retail Invoice in 4 copies',
    'description': """
This modules does Print Tax / Retail Invoice in 4 copies
========================================================
This module adds a new report on invoices for printing retail invoice which will contain more detailed information regarding excise, VAT, TIN etc. specifically used for Indian Localization.

This module was developed by TinyERP Pvt Ltd (OpenERP India). Not covered under OpenERP / Odoo Maintenance Contract or Business Pack. Contact at india@openerp.com if you are looking for support or customization.
""",
    'author': 'Serpent Consulting Services Pvt. Ltd.',
    'website': 'https://www.serpentcs.com',
    'images': [],
    'depends': ['l10n_in_base', 'l10n_in_account_tax', 'l10n_in_dealer_discount_invoice', 'l10n_in_packing_invoice'],
    'data': [
        'report/tax_invoice.xml',
        'view/tax_invoice_view.xml'
    ],
    'installable': True,
    'auto_install': False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
