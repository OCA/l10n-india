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


class stock_move(models.Model):
    _inherit = 'stock.move'

    price_dealer = fields.Float(string='Dealer Price')
    dealer_discount = fields.Float(string='Dealer Discount')
    dealer_discount_per = fields.Float(string='Dealer Discount (%)')

stock_move()


class stock_picking(models.Model):
    _inherit = "stock.picking"
    _table = "stock_picking"

    @api.model
    def _prepare_invoice_line(self, group, picking, move_line, invoice_id,
                              invoice_vals):
        res = super(stock_picking,
                    self)._prepare_invoice_line(group=group,
                                                picking=picking,
                                                move_line=move_line,
                                                invoice_id=invoice_id,
                                                invoice_vals=invoice_vals)
        res = dict(res,
                   price_dealer=(move_line.price_dealer *
                                 move_line.product_qty),
                   dealer_discount=(move_line.dealer_discount *
                                    move_line.product_qty),
                   dealer_discount_per=move_line.dealer_discount_per)
        return res

stock_picking()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
