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

import time
from openerp import models, fields, api
from openerp.tools.translate import _
import openerp.addons.decimal_precision as dp
from openerp.tools import DEFAULT_SERVER_DATE_FORMAT
from openerp.exceptions import Warning


class sale_order_line(models.Model):
    _inherit = 'sale.order.line'

    packaging_cost = fields.Float(string='Packing Cost')

    @api.model
    def _prepare_order_line_invoice_line(self, line, account_id=False):
        res = super(sale_order_line, self
                    )._prepare_order_line_invoice_line(line=line,
                                                       account_id=account_id)
        res = dict(res, packaging_cost=line.packaging_cost)
        return res

    @api.multi
    def product_id_change(self, pricelist, product, qty=0, uom=False,
                          qty_uos=0, uos=False, name='', partner_id=False,
                          lang=False, update_tax=True, date_order=False,
                          packaging=False, fiscal_position=False, flag=False):
        '''
        The purpose of this function to get value of price unit, list price,
        packing amount on product change.
        :return: return this value list price , price unit, packing amount.
        :rtype: dictionary
        '''
        res = super(sale_order_line,
                    self).product_id_change(pricelist, product, qty=qty,
                                            uom=uom, qty_uos=qty_uos, uos=uos,
                                            name=name, partner_id=partner_id,
                                            lang=lang, update_tax=update_tax,
                                            date_order=date_order,
                                            packaging=packaging,
                                            fiscal_position=fiscal_position,
                                            flag=flag)
        product_pool = self.env['product.product']
        package_pool = self.env['product.packaging']

        if not packaging:
            packaging = res.get('value', {}).get('product_packaging', False)

        package_product = False
        qty_factor = 0
        if product:
            package = product_pool.browse(product)
            if package.container_id:
                package_product = package.container_id
                qty_factor = qty

        if not package_product and packaging:
            package = package_pool.browse(packaging)
            if package.ul.container_id:
                package_product = package.ul.container_id
                qty_factor = round(qty / package.qty)
            else:
                raise Warning(_('Warning!'),
                              _("""Unable to compute packaging cost as
                              you have not define product
                              on box %s""" % (package.ul.name)))
        if package_product:
            packing_res = super(sale_order_line,
                                self).product_id_change(pricelist,
                                                        package_product.id,
                                                        qty=1,
                                                        uom=(package_product.
                                                             uom_id.id),
                                                        partner_id=partner_id,
                                                        lang=lang,
                                                        fiscal_position=
                                                        fiscal_position,
                                                        flag=flag)
            res['value']['packaging_cost'] = (qty_factor *
                                              packing_res['value'
                                                          ]['price_unit'])
        else:
            res['value']['packaging_cost'] = 0.0
        return res


class sale_order(models.Model):
    _inherit = 'sale.order'

    @api.multi
    @api.depends('order_line', 'order_line.price_unit', 'order_line.tax_id',
                 'order_line.discount', 'order_line.product_uom_qty',
                 'order_line.packaging_cost', 'round_off')
    def _amount_all(self):
        for order in self:
            val = val1 = val2 = 0.0
            cur = order.pricelist_id.currency_id
            for line in order.order_line:
                val1 += line.price_subtotal
                val += self._amount_line_tax(line)
                val2 += line.packaging_cost
            order.amount_tax = cur.round(val)
            order.amount_untaxed = cur.round(val1)
            order.amount_packing = cur.round(val2)
            order.amount_total = (order.amount_untaxed + order.amount_tax +
                                  order.amount_packing + order.round_off)

    amount_untaxed = fields.Float(compute=_amount_all,
                                  digits_compute=dp.get_precision('Account'),
                                  string='Untaxed Amount',
                                  multi='sums',
                                  help="The amount without tax.",
                                  track_visibility='always')
    amount_tax = fields.Float(compute=_amount_all,
                              digits_compute=dp.get_precision('Account'),
                              string='Taxes',
                              multi='sums', help="The tax amount.")
    amount_total = fields.Float(compute=_amount_all,
                                digits_compute=dp.get_precision('Account'),
                                string='Total',
                                multi='sums', help="The total amount.")
    amount_packing = fields.Float(compute=_amount_all,
                                  digits_compute=dp.get_precision('Account'),
                                  string='Packing Cost',
                                  multi='sums', help="The total amount.")
    round_off = fields.Float(string='Round Off', help="Round Off Amount")

    @api.multi
    def _get_default_values(self, preline):
        res = super(sale_order, self)._get_default_values(preline=preline)
        res = dict(res,packaging_cost=-preline.packaging_cost)
        return res

    @api.model
    def _make_invoice(self, order, lines):
        inv_obj = self.env['account.invoice']
        invoiced_sale_line_ids = self.env['sale.order.line'
                                          ].search([('order_id',
                                                     '=', order.id),
                                                    ('invoiced', '=', True)])
        from_line_invoice_ids = []
        for invoiced_sale_line_id in invoiced_sale_line_ids:
            for invoice_line_id in invoiced_sale_line_id.invoice_lines:
                if invoice_line_id.invoice_id.id not in from_line_invoice_ids:
                    from_line_invoice_ids.append(invoice_line_id.
                                                 invoice_id.id)
        for preinv in order.invoice_ids:
            if (preinv.state not in ('cancel',
                                     ) and preinv.id not in from_line_invoice_ids):
                for preline in preinv.invoice_line:
                    res = self._get_default_values(preline)
                    inv_line_id = preline.copy(res)
                    lines.append(inv_line_id.id)
        inv = self._prepare_invoice(order, lines)
        inv_id = inv_obj.create(inv)
        time_obj = time.strftime(DEFAULT_SERVER_DATE_FORMAT)
        data = inv_id.onchange_payment_term_date_invoice(inv['payment_term'],
                                                         time_obj)
        if data.get('value', False):
            inv_id.write(data['value'])
        inv_id.button_compute([inv_id])
        return inv_id.id

    @api.model
    def _prepare_order_line_move(self, order, line, picking_id, date_planned):
        res = super(sale_order,
                    self)._prepare_order_line_move(order=order, line=line,
                                                   picking_id=picking_id,
                                                   date_planned=date_planned)
        res = dict(res, packaging_cost=line.packaging_cost)
        return res

sale_order()


class sale_advance_payment_inv(models.TransientModel):
    _inherit = 'sale.advance.payment.inv'

    @api.multi
    def _prepare_advance_invoice_vals(self):
        result = super(sale_advance_payment_inv,
                       self)._prepare_advance_invoice_vals()
        sale_obj = self.env['sale.order']
        wizard = self
        sale_ids = self._context.get('active_ids', [])
        update_val = {}
        for sale in sale_obj.browse(sale_ids):
            res = {}
            if wizard.advance_payment_method == 'percentage':
                packing_amount = sale.amount_packing * wizard.amount / 100
            else:
                inv_amount = wizard.amount
                percent = inv_amount / sale.amount_total
                packing_amount = sale.amount_packing * percent / 100
            res = {'packaging_cost': packing_amount
                   }
            update_val[sale.id] = res
        # TODO: Need to re-implement it in best way
        for line in result:
            line[1].get('invoice_line')[0][2].update(update_val.get(line[0]))
        return result

sale_advance_payment_inv()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
