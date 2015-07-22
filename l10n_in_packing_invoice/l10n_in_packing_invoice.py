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

from openerp import fields, models, api
import openerp.addons.decimal_precision as dp


class account_invoice_line(models.Model):
    _inherit = 'account.invoice.line'

    packaging_cost = fields.Float(string='Packing Cost')

    @api.multi
    def product_id_change(self, product, uom_id, qty=0, name='',
                          type='out_invoice', partner_id=False,
                          fposition_id=False, price_unit=False,
                          currency_id=False, company_id=None):
        res = super(account_invoice_line,
                    self).product_id_change(product=product,
                                            uom_id=uom_id, qty=qty, name=name,
                                            type=type, partner_id=partner_id,
                                            fposition_id=fposition_id,
                                            price_unit=price_unit,
                                            currency_id=currency_id,
                                            company_id=company_id)

        product_pool = self.env['product.product']

        res['value']['packaging_cost'] = 0.0
        if product:
            package = product_pool.browse(product)
            if package.container_id:
                res['value']['packaging_cost'] = (package.
                                                  container_id.list_price)
        return res

account_invoice_line()


class account_invoice(models.Model):
    _inherit = 'account.invoice'

    @api.multi
    @api.depends('invoice_line.price_unit',
                 'invoice_line.invoice_line_tax_id', 'invoice_line.quantity',
                 'invoice_line.discount', 'invoice_line.invoice_id',
                 'invoice_line.packaging_cost', 'round_off')
    def _amount_all(self):
        amount_untaxed = 0.0
        amount_tax = 0.0
        amount_total = 0.0
        amount_packing = 0.0
        for invoice in self:
            for line in invoice.invoice_line:
                amount_untaxed = line.price_subtotal + amount_untaxed
                amount_packing = line.packaging_cost + amount_packing
            for line in invoice.tax_line:
                amount_tax = line.amount + amount_tax
            self.amount_untaxed = amount_untaxed
            self.amount_packing = amount_packing
            self.amount_tax = amount_tax
            self.amount_total = (amount_untaxed + amount_packing +
                                 amount_tax + self.round_off)
    amount_untaxed = fields.Float(compute=_amount_all,
                                  digits_compute=dp.get_precision('Account'),
                                  string='Subtotal',
                                  track_visibility='always',
                                  multi='all')
    amount_tax = fields.Float(compute=_amount_all,
                              digits_compute=dp.get_precision('Account'),
                              string='Tax',
                              multi='all')
    amount_total = fields.Float(compute=_amount_all,
                                digits_compute=dp.get_precision('Account'),
                                string='Total',
                                multi='all')
    amount_packing = fields.Float(compute=_amount_all,
                                  digits_compute=dp.get_precision('Account'),
                                  string='Packing Cost',
                                  multi='all')
    round_off = fields.Float(string='Round Off', help="Round Off Amount")

account_invoice()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
