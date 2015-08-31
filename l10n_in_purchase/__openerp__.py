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
    'name' : 'Purchase Management, Indian localization',
    'version' : '1.0',
    'sequence': 111,
    'category': 'Indian Localization',
    'author': 'Serpent Consulting Services Pvt. Ltd.',
    'website': 'https://www.serpentcs.com',
    'summary' : 'Purchase Management, Indian localization',
    'description' : """This modules does
Manage Freight, Packaging & Forwarding, Insurance, Mill Delivery
=====================================================================
This module allows you to manage different charges on Purchase orders & Supplier invoices used for Indian Localization.

* Freight
* Packaging & Forwarding
* Insurance
* Mill Delivery

Management of Rates and Amounts
++++++++++++++++++++++++++++++++++++++
You can manage calculation of various charges by different applicable options.

* **Fix Amount**: Fix amount applicable on total price
* **Percentage**: Amount in percentage applicable on total price
* **Per Unit**: Fix amount applicable per unit on total quantity of items
* **At actual**: Charge different rates over time

Reports
++++++++++
It also prints reports of Purchase orders and Supplier Invoices with Freight/Packaging etc. information.

""",
    'depends' : ['l10n_in_base', 'purchase'],
    'data' : [
    ],
    'update_xml' : ['l10n_in_purchase_view.xml',
                    'l10n_in_account_view.xml',
                    'purchase_report.xml',
                    'report/account_print_invoice.xml',
                    'report/order.xml',
    ],

    'demo': [],

    'installable' : True,
    'application' : False,
}
