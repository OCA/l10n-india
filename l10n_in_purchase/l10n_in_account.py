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
from openerp import fields,models,api,_
from openerp import netsvc
import openerp.addons.decimal_precision as dp

class account_invoice(models.Model):
    _inherit = 'account.invoice'
    
    @api.multi
    @api.depends('invoice_line','package_and_forwording','insurance','freight','round_off','invoice_line.price_unit','invoice_line.invoice_line_tax_id','invoice_line.quantity','invoice_line.discount','invoice_line.invoice_id')
    def _amount_all(self):
        res = {}
        amount_untaxed = 0.0
        amount_tax = 0.0
        amount_total = 0.0
        other_charges = 0.0
        for invoice in self:
            for line in invoice.invoice_line:
                amount_untaxed += line.price_subtotal
            for line in invoice.tax_line:
                amount_tax += line.amount
            self.amount_tax = amount_tax
            self.amount_untaxed = amount_untaxed
            self.other_charges = invoice.package_and_forwording + invoice.insurance + invoice.freight
            self.amount_total = invoice.amount_tax + invoice.amount_untaxed + invoice.other_charges + invoice.round_off
    
    package_and_forwording = fields.Float('Packaging & Forwarding')
    insurance = fields.Float('Insurance')
    freight = fields.Float('Freight')
    round_off = fields.Float('Round Off', help="Round Off Amount")
    delivery_id = fields.Many2one('mill.delivery', 'Mill Delivery')
    amount_untaxed = fields.Float(compute = _amount_all, digits_compute=dp.get_precision('Account'), string='Subtotal', track_visibility='always',
        multi='all')
    amount_tax = fields.Float(compute = _amount_all, digits_compute=dp.get_precision('Account'), string='Tax',
        multi='all')
    amount_total= fields.Float(compute = _amount_all, digits_compute=dp.get_precision('Account'), string='Total',
        multi='all')
    other_charges= fields.Float(compute = _amount_all, digits_compute=dp.get_precision('Account'), string='Other Charges',
        multi='all')
    
account_invoice()