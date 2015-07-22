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

from openerp import models, fields, api
from openerp.tools.translate import _
import openerp.addons.decimal_precision as dp


class account_invoice(models.Model):
    _inherit = 'account.invoice'

    @api.multi
    @api.depends('dealer_pricelist_id', 'invoice_line',
                 'invoice_line.price_unit', 'invoice_line.price_dealer',
                 'invoice_line.product_uom_qty')
    def _total_dealer_disc(self):
        for invoice in self:
            total = 0.0
            for line in invoice.invoice_line:
                total += ((line.price_unit - line.price_dealer) *
                          line.quantity)
            invoice.total_dealer_disc = total

    dealer_id = fields.Many2one('res.partner', string='Dealer', readonly=True,
                                states={'draft':[('readonly', False)]})
    dealer_pricelist_id = fields.Many2one('product.pricelist',
                                          'Dealer Pricelist',
                                          domain=[('type', '=', 'sale')])
    total_dealer_disc = fields.Float(compute='_total_dealer_disc',
                                     digits_compute=dp.
                                     get_precision('Account'),
                                     string='Total Dealer Disc.')

    @api.onchange('dealer_id')
    def onchange_dealer_id(self):
        if not self.dealer_id:
            self.dealer_pricelist_id = False
        val = {}
        pricelist = (self.dealer_id.property_product_pricelist and
                     self.dealer_id.property_product_pricelist.id or False)
        if pricelist:
            self.dealer_pricelist_id = pricelist

account_invoice()


class account_invoice_line(models.Model):
    _inherit = 'account.invoice.line'

    price_dealer = fields.Float(string='Dealer Price')
    dealer_discount = fields.Float(string='Dealer Discount')
    dealer_discount_per = fields.Float(string='Dealer Discount (%)')

    @api.multi
    def product_id_change(self, product, uom_id, qty=0, name='',
                          type='out_invoice', partner_id=False,
                          fposition_id=False, price_unit=False,
                          currency_id=False, company_id=None):
        res = {'value':{}}
        if product:
            res = super(account_invoice_line,
                        self).product_id_change(product, uom_id, qty, name,
                                                type, partner_id=partner_id,
                                                fposition_id=fposition_id,
                                                price_unit=price_unit,
                                                currency_id=currency_id,
                                                company_id=company_id)
            pricelist_pool = self.env['product.pricelist']
            context = self._context
            dealer_id = context.get('dealer_id')
            dealer_pricelist_id = context.get('dealer_pricelist_id')
            if dealer_id and dealer_pricelist_id:
                dealer_res = pricelist_pool.price_get(product, qty, dealer_id)
                price_unit = res['value']['price_unit']
                price_dealer = dealer_res.get(dealer_pricelist_id)
                dealer_discount = price_unit - price_dealer
                res['value']['price_dealer'] = price_dealer * qty
                res['value']['dealer_discount'] = dealer_discount * qty
                res['value']['dealer_discount_per'
                             ] = (dealer_discount * 100) / price_unit
        return res

account_invoice_line()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
