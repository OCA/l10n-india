# -*- coding: utf-8 -*-
##############################################################################
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
##############################################################################

import logging

from openerp import models, fields

_logger = logging.getLogger(__name__)

class indian_base_configuration(models.TransientModel):

    _name = 'indian.base.config.settings'
    _inherit = 'res.config.settings'

    module_product_coding = fields.Boolean(string='Define automatic codings on products',
    help="""Allows you to keeps track of internal material request.
        It installs the stock_indent module.""")
    group_major_sub_group_config = fields.Boolean(string='Allows to configure Major and Sub Groups', implied_group='l10n_in_base.group_major_sub_group_config', help="""TODO""")
    module_product_container = fields.Boolean(string='Define container or packaging and repairable products',
    help="""Allows gate keeper to pass the outgoing materials, products, etc. and keeps track of returning items.
        It installs the stock_gatepass module.""")

    default_coding_method = fields.Selection(selection=[('category', 'Based on the Category'), ('group', 'Based on Major / Sub Groups')], required=True, default_model='product.product', default='category')

    module_stock_indent = fields.Boolean(string='Manage internal requests for material, service through Indents.',
    help="""Allows you to keeps track of internal material request.
        It installs the stock_indent module.""")
    module_stock_gatepass = fields.Boolean(string='Track outgoing material through Gatepass',
    help="""Allows gate keeper to pass the outgoing materials, products, etc. and keeps track of returning items.
        It installs the stock_gatepass module.""")

    module_stock_serial_tracking = fields.Boolean(string='Track products by location on serial numbers',
    help="""Allows you to keeps track of internal material request.
        It installs the stock_indent module.""")
    module_product_container_tracking = fields.Boolean(string='Track container and its movement in warehouse',
    help="""Allows you to keeps track of internal material request.
        It installs the stock_indent module.""")

    module_stock_indent_gatepass = fields.Boolean(string='Track your machine or material sent outside company for repairing, with approvals',
    help="""Allows you to keeps track of internal material request.
        It installs the stock_indent module.""")
    module_stock_sale_gatepass = fields.Boolean(string='Track your returnable containers you deliver with products',
    help="""Allows you to keeps track of internal material request.
        It installs the stock_indent module.""")

    module_l10n_in_excise_receipt = fields.Boolean(string='Manage excise on Incoming Shipments and prepare Invoice based on Excise Receipt',
    help="""Allows you to keeps track of internal material request.
        It installs the stock_indent module.""")
    module_quotation_template = fields.Boolean(string='Prepare bundle offers with templates quotation',
    help="""Allows you to keeps track of internal material request.
        It installs the stock_indent module.""")
    module_sale_after_service = fields.Boolean(string='Manage after sale service using service contracts for products',
    help="""Allows you to keeps track of internal material request.
        It installs the stock_indent module.""")

    module_l10n_in_account_tax = fields.Boolean(string='Manage categories on Tax to differentiate taxes as per Indian Taxonomy',
    help="""Allows you to keeps track of internal material request.
        It installs the stock_indent module.""")
    module_l10n_in_invoice_adjust = fields.Boolean(string='Adjust payable and receivables with each other using vouchers',
    help="""Allows you to keeps track of internal material request.
        It installs the stock_indent module.""")

    module_attachment_size_limit = fields.Boolean(string='Restrict on size of attachments and users for attachments',
    help="""Allows you to keeps track of internal material request.
        It installs the stock_indent module.""")
    module_web_group_expand = fields.Boolean(string='Enable expand and collapse features on group by list view',
    help="""Allows you to keeps track of internal material request.
        It installs the stock_indent module.""")

    module_l10n_in_sales_packing = fields.Boolean(string='Add packaging cost on sales order line, to compute the packaging cost for product',
    help="""Allows you to keeps track of internal material request.
        It installs the stock_indent module.""")

    module_l10n_in_dealers_discount = fields.Boolean(string='Add dealer discount on sales order line, to compute the commission for dealer',
    help="""Allows you to keeps track of internal material request.
        It installs the stock_indent module.""")

    module_l10n_in_packing_stock_invoice = fields.Boolean(string='Transfer Packaging cost on customer invoice when invoice prepared based on Delivery Order',
    help="""Allows you to keeps track of internal material request.
        It installs the stock_indent module.""")

    module_l10n_in_dealer_discount_stock_invoice = fields.Boolean(string='Transfer Dealers discount on customer invoice when invoice prepared based on Delivery Order',
    help="""Allows you to keeps track of internal material request.
        It installs the stock_indent module.""")

    module_l10n_in_tax_retail_invoice = fields.Boolean(string='Print Tax / Retail Invoice in 4 copies',
    help="""Allows you to keeps track of internal material request.
        It installs the stock_indent module.""")

    module_l10n_in_excise_invoice = fields.Boolean(string='Print Excise Invoice in 4 copies',
    help="""Allows you to keeps track of internal material request.
        It installs the stock_indent module.""")

    module_l10n_in_dealer_discount_invoice = fields.Boolean(string='Compute Dealer Discount on Invoice',
    help="""Allows you to keeps track of internal material request.
        It installs the stock_indent module.""")
    module_l10n_in_packing_invoice = fields.Boolean(string='Compute Packaging Cost on Invoice',
    help="""Allows you to keeps track of internal material request.
        It installs the stock_indent module.""")

    module_purchase_crm = fields.Boolean(string='Get the Supplier price before proposing to Customer on Opportunity',
    help="""Allows you to keeps track of internal material request.
        It installs the stock_indent module.""")

    group_cst_config = fields.Boolean(string='Enable Central Sales Tax on Partners', implied_group='l10n_in_base.group_cst_config', help="""TODO""")
    group_excise_config = fields.Boolean(string='Enable Excise Control Code on Partners', implied_group='l10n_in_base.group_excise_config', help="""TODO""")
    group_tin_config = fields.Boolean(string='Enable Tax Identification Number on Partners', implied_group='l10n_in_base.group_tin_config', help="""TODO""")
    group_service_config = fields.Boolean(string='Enable Service Tax Number on Partner', implied_group='l10n_in_base.group_service_config', help="""TODO""")

    module_l10n_in_purchase = fields.Boolean(string='Additional feature and computation on purchase orders',
    help="""Allows you to keeps track of internal material request.
        It installs the stock_indent module.""")

    group_packing_config = fields.Boolean(string='Allow Packaging and Forwarding charges on Purchase', implied_group='l10n_in_base.group_packing_config', help="""TODO""")
    group_freight_config = fields.Boolean(string='Allow Fright charges on Purchase', implied_group='l10n_in_base.group_freight_config', help="""TODO""")
    group_insurance_config = fields.Boolean(string='Allow Insurance charges on Purchase', implied_group='l10n_in_base.group_insurance_config', help="""TODO""")

    group_discount_purchase_config = fields.Boolean(string='Allow Discount on Purchase Order lines', implied_group='l10n_in_base.group_discount_purchase_config', help="""TODO""")

    group_round_off_purchase_config = fields.Boolean(string='Round-off feature on Purchase Order', implied_group='l10n_in_base.group_round_off_purchase_config', help="""TODO""")
    group_round_off_sale_config = fields.Boolean(string='Round-off feature on Sales Order', implied_group='l10n_in_base.group_round_off_sale_config', help="""TODO""")

    group_dealer_price_on_sale_config = fields.Boolean(string='Display dealer price on sales order line', implied_group='l10n_in_base.group_dealer_price_on_sale_config', help="""TODO""")
    group_inter_state_tax_config = fields.Boolean(string='Maintain Register of Forms to be issue and to be receive for Inter-State, Intet-Warehouse or Export Sales', implied_group='l10n_in_base.group_inter_state_tax_config', help="""i.e. C-Form, H-Form, E1-Form, etc""")

    group_invoice_types_config = fields.Boolean(string='Allow to have different types on Invoices and printing based on Types', implied_group='l10n_in_base.group_invoice_types_config', help="""TODO""")

indian_base_configuration()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
