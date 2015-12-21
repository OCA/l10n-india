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

from openerp import fields, models
import logging

_logger = logging.getLogger(__name__)


class IndianBaseConfiguration(models.TransientModel):
    _inherit = 'res.config.settings'

    _name = 'indian.base.config.settings'

    module_product_coding =\
        fields.Boolean('Define automatic codings on products',
                       help="""Allows you to keeps track of
                       internal material request. It installs
                       the product_coding module.""")
    group_major_sub_group =\
        fields.Boolean('Allows to configure Major and Sub Groups',
                       implied_group='l10n_in_base.group_major_sub_group',
                       help="Allows to configure Major and Sub Groups.")
    module_product_container =\
        fields.Boolean('Define container or packaging and repairable products',
                       help="""Allows gate keeper to pass the outgoing
                       materials, products, etc. and keeps track of returning
                       items. It installs the product_container module.""")
    default_coding_method =\
        fields.Selection([('category', 'Based on the Category'),
                          ('group', 'Based on Major / Sub Groups')],
                         required=True, default_model='product.product',
                         default='category')
    module_stock_indent =\
        fields.Boolean("""Manage internal requests for material,
                       service through Indents.""",
                       help="""Allows you to keeps track of internal material
                       request. It installs the stock_indent module.""")
    module_stock_gatepass =\
        fields.Boolean('Track outgoing material through Gatepass',
                       help="""Allows gate keeper to pass the outgoing
                       materials, products, etc. and keeps track of returning
                       items. It installs the stock_gatepass module.""")
    module_stock_serial_tracking =\
        fields.Boolean('Track products by location on serial numbers',
                       help="""Allows you to keeps track
                       of internal material request. It
                       installs the stock_serial_tracking module.""")
    module_product_container_tracking =\
        fields.Boolean('Track container and its movement in warehouse',
                       help="""Allows you to keeps track of internal material
                       request. It installs the product_container_tracking
                       module.""")
    module_stock_indent_gatepass =\
        fields.Boolean("""Track your machine or material sent outside company
                       for repairing, with approvals""",
                       help="""Allows you to keeps track of internal material
                       request. It installs the stock_indent_gatepass
                       module.""")
    module_stock_sale_gatepass =\
        fields.Boolean('Track your returnable containers you deliver with\
                       products',
                       help="""Allows you to keeps track of internal material\
                       request. It installs the stock_sale_gatepass module.""")
    module_l10n_in_excise_receipt =\
        fields.Boolean("""Manage excise on Incoming Shipments and prepare
                       Invoice based on Excise Receipt""",
                       help="""Allows you to keeps track of internal material
                       request. It installs the l10n_in_excise_receipt
                       module.""")
    module_quotation_template =\
        fields.Boolean('Prepare bundle offers with templates quotation',
                       help="""Allows you to keeps track of internal material
                       request. It installs the quotation_template module.""")
    module_sale_after_service =\
        fields.Boolean("""Manage after sale service using service contracts
                       for products""",
                       help="""Allows you to keeps track of internal material
                       request. It installs the sale_after_service module.""")
    module_l10n_in_account_tax =\
        fields.Boolean("""Manage categories on Tax to differentiate taxes
                       as per Indian Taxonomy""",
                       help="""Allows you to keeps track of internal material
                       request. It installs the l10n_in_account_tax module.""")
    module_l10n_in_invoice_adjust =\
        fields.Boolean("""Adjust payable and receivables with each other
                       using vouchers""",
                       help="""Allows you to keeps track of internal
                       material request. It installs the
                       l10n_in_invoice_adjust module.""")
    module_attachment_size_limit =\
        fields.Boolean('Restrict on size of attachments and users \
                       for attachments',
                       help="""Allows you to keeps track of
                       internal material request.
                       It installs the attachment_size_limit module.""")
    module_web_group_expand =\
        fields.Boolean('Enable expand and collapse features on \
                       group by list view',
                       help="""Allows you to keeps track of internal material
                       request. It installs the web_group_expand module.""")
    module_l10n_in_sales_packing =\
        fields.Boolean("""Add packaging cost on sales order line,
                       to compute the packaging cost for product""",
                       help="""Allows you to keeps track
                       of internal material request. It installs
                       the l10n_in_sales_packing module.""")
    module_l10n_in_dealers_discount =\
        fields.Boolean("""Add dealer discount on sales order line,
                       to compute the commission for dealer""",
                       help="""Allows you to keeps track
                       of internal material request.It installs
                       the l10n_in_dealers_discount module.""")
    module_l10n_in_packing_stock_invoice =\
        fields.Boolean("""Transfer Packaging cost on customer invoice
                       when invoice prepared based on Delivery Order""",
                       help="""Allows you to keeps track
                       of internal material request. It installs
                       the l10n_in_packing_stock_invoice module.""")
    module_l10n_in_dealer_discount_stock_invoice =\
        fields.Boolean("""Transfer Dealers discount on customer invoice
                       when invoice prepared based on Delivery Order""",
                       help="""Allows you to keeps track
                       of internal material request. It installs
                       the l10n_in_dealer_discount_stock_invoice module.""")
    module_l10n_in_tax_retail_invoice =\
        fields.Boolean('Print Tax / Retail Invoice in 4 copies',
                       help="""Allows you to keeps track
                       of internal material request. It installs
                       the l10n_in_tax_retail_invoice module.""")
    module_l10n_in_excise_invoice =\
        fields.Boolean('Print Excise Invoice in 4 copies',
                       help="""Allows you to keeps track
                       of internal material request. It installs
                       the l10n_in_excise_invoice module.""")
    module_l10n_in_dealer_discount_invoice =\
        fields.Boolean('Compute Dealer Discount on Invoice',
                       help="""Allows you to keeps track
                       of internal material request. It installs
                       the l10n_in_dealer_discount_invoice module.""")
    module_l10n_in_packing_invoice =\
        fields.Boolean('Compute Packaging Cost on Invoice',
                       help="""Allows you to keeps track
                       of internal material request. It installs
                       the l10n_in_packing_invoice module.""")
    module_purchase_crm =\
        fields.Boolean("""Get the Supplier price before proposing
                       to Customer on Opportunity""",
                       help="""Allows you to keeps track
                       of internal material request. It installs
                       the purchase_crm module.""")
    group_cst_config =\
        fields.Boolean('Enable Central Sales Tax on Partners',
                       implied_group='l10n_in_base.group_cst_config')
    group_excise_config =\
        fields.Boolean('Enable Excise Control Code on Partners',
                       implied_group='l10n_in_base.group_excise_config')
    group_tin_config =\
        fields.Boolean('Enable Tax Identification Number on Partners',
                       implied_group='l10n_in_base.group_tin_config')
    group_service_config =\
        fields.Boolean('Enable Service Tax Number on Partner',
                       implied_group='l10n_in_base.group_service_config')
    module_l10n_in_purchase =\
        fields.Boolean('Additional feature and computation on purchase orders',
                       help="""Allows you to keeps track of internal material
                       request. It installs the stock_indent module.""")
    group_packing_config =\
        fields.Boolean('Allow Packaging and Forwarding charges on Purchase',
                       implied_group='l10n_in_base.group_packing_config')
    group_freight_config =\
        fields.Boolean('Allow Fright charges on Purchase',
                       implied_group='l10n_in_base.group_freight_config')
    group_insurance_config =\
        fields.Boolean('Allow Insurance charges on Purchase',
                       implied_group='l10n_in_base.group_insurance_config')
    group_discount_purchase =\
        fields.Boolean('Allow Discount on Purchase Order lines',
                       implied_group='l10n_in_base.group_discount_purchase')
    group_round_off_purchase =\
        fields.Boolean('Round-off feature on Purchase Order',
                       implied_group='l10n_in_base.group_round_off_purchase')
    group_round_off_sale =\
        fields.Boolean('Round-off feature on Sales Order',
                       implied_group='l10n_in_base.group_round_off_sale')
    group_dealer_price_on_sale =\
        fields.Boolean('Display dealer price on sales order line',
                       implied_group='l10n_in_base.group_dealer_price_on_sale')
    group_inter_state_tax =\
        fields.Boolean("""Maintain Register of Forms to be issue
                       and to be receive for Inter-State,
                       Intet-Warehouse or Export Sales""",
                       implied_group='l10n_in_base.group_inter_state_tax',
                       help="""i.e. C-Form, H-Form, E1-Form, etc""")
    group_invoice_types_config =\
        fields.Boolean("""Allow to have different types on Invoices and
                       printing based on Types""",
                       implied_group='l10n_in_base.group_invoice_types_config')
