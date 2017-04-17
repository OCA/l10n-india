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

import time
from openerp.osv import osv
from openerp.report import report_sxw

class tax_invoice(report_sxw.rml_parse):

    def __init__(self, cr, uid, name, context=None):
        super(tax_invoice, self).__init__(cr, uid, name, context=context)
        self.localcontext.update({
            'time': time,
            'amount_to_text': self._amount_to_text,
            'get_quantity': self._get_quantity,
            'convert_int': self._convert_int,
        })

    def _amount_to_text(self, amount, currency):
        account_invoice_obj = self.pool.get('account.invoice')
        val = account_invoice_obj.amount_to_text(amount, currency)
        return val

    def _get_quantity(self, id):
        account_invoice_obj = self.pool.get('account.invoice')
        val = account_invoice_obj._get_qty_total(self.cr, self.uid, self.ids)
        return int(val.values()[0])

    def _convert_int(self, amount):
        amount = int(amount)
        return amount

class invoice_tax(osv.AbstractModel):
    _name = 'report.l10n_in_tax_retail_invoice.account_invoice_tax_excise'
    _inherit = 'report.abstract_report'
    _template = 'l10n_in_tax_retail_invoice.account_invoice_tax_excise'
    _wrapped_report_class = tax_invoice

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
