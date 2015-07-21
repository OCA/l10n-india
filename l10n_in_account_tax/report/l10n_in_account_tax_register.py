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

from openerp import models,fields,api
from openerp import tools

TAX_TYPES = [('excise', 'Central Excise'),
    ('cess', 'Cess'),
    ('hedu_cess', 'Higher Education Cess'),
    ('vat', 'VAT'),
    ('add_vat','Additional VAT'),
    ('cst', 'Central Sales Tax'),
    ('service', 'Service Tax'),
    ('tds','Tax Deducted at Source'),
    ('tcs','Tax Collected at Source'),
    ('cform','C Form'),
    ('dform','D Form'),
    ('e1form', 'E1 Form'),
    ('e2form', 'E2 Form'),
    ('fform','F Form'),
    ('hform','H Form'),
    ('iform', 'I Form'),
    ('jform', 'J Form'),
    ('import_duty','Import Duty'),
    ('other', 'Other')
]


class stock_indent_analysis_report(models.Model):

    _name = "account.tax.register"
    _description = "Tax Register"
    _auto = False

    id = fields.Integer('ID')
    invoice_id = fields.Many2one('account.invoice', 'Invoice')
    company_id = fields.Many2one('res.company', 'Company')
    base_amount = fields.Float('Tax Base')
    tax_amount = fields.Float('Tax')
    tax_code_id = fields.Many2one('account.tax.code', 'Tax Code')
    name = fields.Char('Name')
    tax_categ = fields.Selection(TAX_TYPES, 'Tax Category')
    is_form = fields.Boolean('Inter-State Tax')
    form_no = fields.Char('Form No')
    date_iseeu = fields.Date('Issue Date')
    date_invoice = fields.Date('Invoice Date')
    partner_id = fields.Many2one('res.partner', 'Partner')
    amount_untaxed = fields.Float('Invoice Amount')
    gender = fields.Selection(selection=[
             ('male','Male'),
             ('female','Female')],
             string='Gender')
    type = fields.Selection(selection=[
           ('out_invoice','Customer Invoice'),
           ('in_invoice','Supplier Invoice'),
           ('out_refund','Customer Refund'),
           ('in_refund','Supplier Refund'),
           ], string='Type', readonly=True, select=True, change_default=True,
           track_visibility='always')
    state = fields.Selection(selection=[
           ('draft','Draft'),
           ('proforma','Pro-forma'),
           ('proforma2','Pro-forma'),
           ('open','Open'),
           ('paid','Paid'),
           ('cancel','Cancelled'),
           ],string='Status', select=True, readonly=True,
           track_visibility='onchange')
    number = fields.Char('Number')
    cst_no = fields.Char('CST No')

    def init(self, cr):
        tools.drop_view_if_exists(cr, 'account_tax_register')
        cr.execute("""CREATE OR REPLACE view account_tax_register AS (
            select
                t.id as id,
                t.invoice_id as invoice_id,
                t.company_id as company_id,
                t.base_amount as base_amount,
                t.tax_amount as tax_amount,
                t.tax_code_id as tax_code_id,
                t.name as name,
                t.tax_categ as tax_categ,
                t.is_form as is_form,
                t.form_no as form_no,
                t.date_iseeu as date_iseeu,
                i.date_invoice as date_invoice,
                i.partner_id as partner_id,
                i.amount_total as amount_untaxed,
                i.type as type,
                i.state as state,
                i.number as number,
                p.cst_no as cst_no
            from
                account_invoice_tax t
                left join account_invoice i on (t.invoice_id=i.id)
                left join res_partner p on (i.partner_id=p.id)
            )""")
stock_indent_analysis_report()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
