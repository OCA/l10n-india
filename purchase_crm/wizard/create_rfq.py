# -*- coding: utf-8 -*-
############################################################################
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
from openerp import fields, models, api
from openerp.tools.translate import _
import time


class crm_make_purchase(models.TransientModel):

    _name = 'crm.make.purchase'
    _description = 'Opportunity To Purchase Quotation'

    partner_id = fields.Many2one('res.partner', 'Supplier', required=True)
    product_ids = fields.Many2many('product.product', 'opportunity_prod_rel',
                                   'opp_id', 'product_id', 'Products',
                                   required=True)
    warehouse_id = fields.Many2one('stock.warehouse', 'Warehouse',
                                   required=True)

    @api.multi
    def convert_to_rfq(self):
        """
        This function  Create an Quotation on given opportunity.
        @param self: The object pointer
        @param cr: the current row, from the database cursor,
        @param uid: the current user’s ID for security checks,
        @param ids: List of crm make sales' ids
        @param context: A standard dictionary for contextual values
        @return: Dictionary value of created purchase order.
        """

        case_obj = self.env['crm.lead']
        purchase_obj = self.env['purchase.order']
        purchase_line_obj = self.env['purchase.order.line']
        product_obj = self.env['product.product']
        opp_ids = self._context and self._context.get('active_ids', [])

        for opportunity in self:
            partner = opportunity.partner_id
            partner_addr = partner.address_get(['default'])
            pricelist = partner.property_product_pricelist_purchase.id
            fpos = (partner.property_account_position and
                    partner.property_account_position.id or False)
            case = case_obj.browse(opp_ids and opp_ids[0] or [])
            location_id = self.env['stock.warehouse'
                                   ].browse(opportunity.
                                            warehouse_id.
                                            id).wh_input_stock_loc_id.id
            date = time.strftime('%Y-%m-%d')
            vals = {
                'origin': _('Opportunity - ID: %s') % str(case.id),
                'section_id': case.section_id and case.section_id.id or False,
                'partner_id': partner.id,
                'partner_address_id': partner_addr['default'],
                'pricelist_id': pricelist,
                'date_order': date,
                'fiscal_position': fpos,
                'location_id': location_id,
                'warehouse_id': opportunity.warehouse_id.id,
            }
            dt = time.strftime('%Y-%m-%d %H:%M:%S')
            if partner.id:
                vals['user_id'] = (partner.user_id and partner.user_id.id or
                                   self._uid)
            new_id = purchase_obj.create(vals)
            case.write({'ref2': 'purchase.order,%s' % new_id.id})
            for product_id in opportunity.product_ids:
                product = product_obj.browse(product_id.id)
                res = self.env['purchase.order.line'
                               ].onchange_product_id(pricelist,
                                                     product.id, 1,
                                                     product.uom_id.id,
                                                     partner.id,
                                                     date_order=dt)
                res = res['value']
                line_vals = {
                    'name': res['name'],
                    'product_id': product.id,
                    'order_id': new_id.id,
                    'price_unit': res['price_unit'],
                    'date_planned': res['date_planned'],
                    'product_uom': res['product_uom'],
                    'taxes_id': [(6, 0, res['taxes_id'])],
                }
                purchase_line_obj.create(line_vals)

        result = {
            'name': 'Request For Quotation',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'purchase.order',
            'view_id': False,
            'type': 'ir.actions.act_window',
            'res_id': new_id.id
        }
        return result

crm_make_purchase()