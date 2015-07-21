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

from openerp import tools
from openerp import models, fields, api
from openerp.addons.decimal_precision import decimal_precision as dp


class annexure_2b_report(models.Model):
    _name = "annexure.2b.report"
    _description = "Annexure 2B Report"
    _auto = False

    id = fields.Integer('ID')
    account_id = fields.Many2one('account.account', 'Tax Account')
    invoice_id = fields.Many2one('account.invoice', 'Invoice')
    partner_id = fields.Many2one('res.partner', 'Partner')
    tin_no = fields.Char('Tin No.', size=64)
    date = fields.Date('Date')
    base = fields.Float('Base', digits_compute=dp.get_precision('Account'))
    amount = fields.Float('Amount',
                          digits_compute=dp.get_precision('Account'))
    base_code_id = fields.Many2one('account.tax.code', 'Base Code')
    base_amount = fields.Float('Base Code Amount',
                               digits_compute=dp.get_precision('Account'))
    tax_code_id = fields.Many2one('account.tax.code', 'Tax Code')
    tax_amount = fields.Float('Tax Code Amount',
                              digits_compute=dp.get_precision('Account'))

    def init(self, cr):
        tools.drop_view_if_exists(cr, 'annexure_2b_report')
        cr.execute("""CREATE OR REPLACE view annexure_2b_report AS (
            select
                row_number() OVER () AS id,
                ai.date_invoice AS date,
                ai.partner_id as partner_id,
                rp.tin_no as tin_no,
                ait.invoice_id as invoice_id,
                ait.account_id as account_id,
                ait.base as base,
                ait.amount as amount,
                ait.base_code_id as base_code_id,
                ait.base_amount as base_amount,
                ait.tax_code_id as tax_code_id,
                ait.tax_amount as tax_amount

            FROM 
                account_invoice_line ail
                LEFT JOIN account_invoice ai ON (ail.invoice_id = ai.id)
                LEFT JOIN account_invoice_tax ait ON (ait.invoice_id = ai.id)
                LEFT JOIN res_partner rp ON (ai.partner_id = rp.id)

                WHERE ai.type = 'out_invoice'
                GROUP BY ail.id,
                ai.date_invoice,
                ai.partner_id,
                rp.tin_no,
                ail.account_id,
                ait.invoice_id,
                ait.account_id,
                ait.base,
                ait.amount,
                ait.base_amount,
                ait.tax_amount,
                ait.base_code_id,
                ait.tax_code_id
                )""")

annexure_2b_report()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
