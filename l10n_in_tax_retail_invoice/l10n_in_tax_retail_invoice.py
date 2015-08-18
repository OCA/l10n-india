# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2012-Today Serpent Consulting Services Pvt. Ltd. (<http://www.serpentcs.com>)
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
from openerp import models, fields, api, _
from openerp.tools.amount_to_text_en import amount_to_text

class account_invoice(models.Model):
    _inherit = 'account.invoice'
    
    @api.model
    def _get_qty_total(self,ids):
        res = {}
        qty = 0.0
        for invoice in self.browse(ids):
            for line in invoice.invoice_line:
                qty += line.quantity
            res[invoice.id] = qty
        return res

    @api.model
    def amount_to_text(self, amount, currency):
        '''
        The purpose of this function is to use payment amount change in word
        @param amount: pass Total payment of amount
        @param currency: pass which currency to pay
        @return: return amount in word
        @rtype : string
        '''
        amount_in_word = amount_to_text(amount)
        if currency == 'INR':
            amount_in_word = amount_in_word.replace("euro", "Rupees").replace("Cents", "Paise").replace("Cent", "Paise")
        return amount_in_word

    delivery_address_id = fields.Many2one('res.partner',string='Delivery Address')

account_invoice()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
