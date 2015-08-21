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
    'name': 'Dealer Price on Invoice',
    'version': '1.0',
    'category': 'Indian Localization',
    'summary': 'Dealer Price, Compute discount for Dealers on Invoice',
    'description': """Dealer Price on Invoice
=================================================================
With the use of this module you can define dealer specific price
with the use of dealer's pricelist. On the Invoice you can select
the dealer and the relevant pricelist so from the invoice you can get
the dealer price amount along with the customer price amount.
""",
    'author': 'Serpent Consulting Services Pvt. Ltd.',
    'website': 'https://www.serpentcs.com',
    'depends': ['l10n_in_base', 'product_container', 'account'],
    'data': ['l10n_in_dealer_discount_invoice.xml'],
    'installable': True,
    'auto_install': False,
}