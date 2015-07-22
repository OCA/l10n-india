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
import time
from openerp import models, fields, api
from openerp.tools import DEFAULT_SERVER_DATE_FORMAT


class sale_order_line(models.Model):
    _inherit = 'sale.order.line'

    price_dealer = fields.Float(string='Dealer Price', readonly=True,
                                select=True,
                                states={'draft': [('readonly', False)],
                                        'sent': [('readonly', False)]})
    dealer_discount = fields.Float(string='Dealer Discount', readonly=True,
                                   select=True,
                                   states={'draft': [('readonly', False)],
                                           'sent': [('readonly', False)]})
    dealer_discount_per = fields.Float(string='Dealer Discount (%)',
                                       readonly=True, select=True,
                                       states={'draft': [('readonly', False)],
                                               'sent': [('readonly', False)]})

    @api.model
    def _prepare_order_line_invoice_line(self, line, account_id=False):
        res = super(sale_order_line,
                    self)._prepare_order_line_invoice_line(line, account_id)
        res = dict(res, price_dealer=line.price_dealer * line.product_uom_qty,
                   dealer_discount=(line.dealer_discount *
                                    line.product_uom_qty),
                   dealer_discount_per=line.dealer_discount_per / 100)
        return res

    @api.multi
    def product_id_change(self, pricelist, product, qty=0, uom=False,
                          qty_uos=0, uos=False, name='', partner_id=False,
                          lang=False, update_tax=True, date_order=False,
                          packaging=False, fiscal_position=False, flag=False,
                          context=None):
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
                                            flag=flag, context=context)
        context = self._context
        dealer_id = context.get('dealer_id')
        dealer_pricelist_id = context.get('dealer_pricelist_id')
        if dealer_id and dealer_pricelist_id:
            dealer_res = super(sale_order_line,
                               self).product_id_change(dealer_pricelist_id,
                                                       product, qty=qty,
                                                       uom=uom,
                                                       qty_uos=qty_uos,
                                                       uos=uos, name=name,
                                                       partner_id=dealer_id,
                                                       lang=lang,
                                                       update_tax=False,
                                                       date_order=date_order,
                                                       packaging=False,
                                                       fiscal_position =\
                                                       fiscal_position,
                                                       flag=flag,
                                                       context=context)
            price_unit = res['value']['price_unit']
            price_dealer = dealer_res['value']['price_unit']
            dealer_discount = price_unit - price_dealer
            res['value']['price_dealer'] = price_dealer
            res['value']['dealer_discount'] = dealer_discount
            res['value']['dealer_discount_per'] = (dealer_discount *
                                                   100) / price_unit
        return res

sale_order_line()


class sale_order(models.Model):
    _inherit = 'sale.order'

    dealer_id = fields.Many2one('res.partner', 'Dealer')
    dealer_pricelist_id = fields.Many2one('product.pricelist',
                                          'Dealer Pricelist',
                                          domain=[('type', '=', 'sale')])

    @api.onchange('dealer_id')
    def onchange_dealer_id(self):
        if not self.dealer_id:
            self.dealer_pricelist_id = False

        pricelist = (self.dealer_id.property_product_pricelist and
                     self.dealer_id.property_product_pricelist.id or False)
        if pricelist:
            self.dealer_pricelist_id = pricelist

    @api.multi
    def _get_default_values(self, preline):
        res = super(sale_order, self)._get_default_values(preline=preline)
        res = dict(res,
                   price_dealer=-preline.price_dealer,
                   dealer_discount=-preline.dealer_discount,
                   dealer_discount_per=-preline.dealer_discount_per
                   )
        return res

    @api.model
    def _make_invoice(self, order, lines):
        inv_obj = self.env['account.invoice']
        invoiced_sale_line_ids = self.env['sale.order.line'
                                          ].search([('order_id',
                                                     '=', order.id),
                                                    ('invoiced', '=', True)])
        from_inv = []
        for invoiced_sale_line_id in invoiced_sale_line_ids:
            for invoice_line_id in invoiced_sale_line_id.invoice_lines:
                if invoice_line_id.invoice_id.id not in from_inv:
                    from_inv.append(invoice_line_id.invoice_id.id)
        for preinv in order.invoice_ids:
            if preinv.state not in ('cancel',) and preinv.id not in from_inv:
                for preline in preinv.invoice_line:
                    res = self._get_default_values(preline)
                    inv_line_id = preline.copy(res)
                    lines.append(inv_line_id.id)
        inv = self._prepare_invoice(order, lines)
        inv.update({'dealer_id': order.dealer_id.id})
        inv_id = inv_obj.create(inv)
        time_obj = time.strftime(DEFAULT_SERVER_DATE_FORMAT)
        data = inv_id.onchange_payment_term_date_invoice(inv['payment_term'],
                                                         time_obj)
        if data.get('value', False):
            inv_id.write(data['value'])
        inv_id.button_compute([inv_id.id])
        return inv_id.id

sale_order()


class sale_advance_payment_inv(models.TransientModel):
    _inherit = 'sale.advance.payment.inv'

    @api.multi
    def _prepare_advance_invoice_vals(self):
        result = super(sale_advance_payment_inv,
                       self)._prepare_advance_invoice_vals()
        sale_obj = self.env['sale.order']
        sale_ids = self._context.get('active_ids', [])
        update_val = {}
        for sale in sale_obj.browse(sale_ids):
            total_price_dealer = total_dealer_discount = 0.0
            price_dealer = dealer_discount = 0.0
            for line in sale.order_line:
                total_price_dealer += line.price_dealer * line.product_uom_qty
                total_dealer_discount += (line.dealer_discount *
                                          line.product_uom_qty)
            res = {}
            total_amount = 0.0
            if self.advance_payment_method == 'percentage':
                price_dealer = total_price_dealer * (self.amount / 100)
                dealer_discount = total_dealer_discount * (self.amount / 100)
                total_amount = (sale.amount_total * self.amount) / 100
            else:
                inv_amount = self.amount
                percent = inv_amount / sale.amount_total
                total_amount = inv_amount
                price_dealer = total_price_dealer * percent
                dealer_discount = total_dealer_discount * percent
            res['price_dealer'] = price_dealer
            res['dealer_discount'] = dealer_discount
            res['dealer_discount_per'] = dealer_discount / total_amount

            update_val[sale.id] = res

        # TODO: Need to re-implement it in best way
        for line in result:
            line[1].get('invoice_line')[0][2].update(update_val.get(line[0]))
        return result

sale_advance_payment_inv()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
