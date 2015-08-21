# -*- coding: utf-8 -*-
############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2011-Today Serpent Consulting Services Pvt. Ltd.
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
import re
from openerp import models, fields, api
from openerp.tools.translate import _
from openerp import tools
from openerp.exceptions import Warning


class sale_order(models.Model):
    _inherit = 'sale.order'

    is_template = fields.Boolean(string='Template')
    template_id = fields.Many2one('sale.order', 'Offer',
                                  domain=[('is_template', '=', True)])

    @api.onchange('template_id')
    def onchange_template(self):
        line_obj = self.env['sale.order.line']
        result = {'order_line': []}
        lines = []

        if not self.template_id:
            self.template_id = result

        if not self.partner_id:
            raise Warning(_('No Customer Defined!'),
                          _("""Before choosing a template,\n
                          select a customer in the template form."""))

        order_lines = self.template_id.order_line
        for line in order_lines:
            vals = line_obj.product_id_change(
                pricelist=self.pricelist_id.id,
                product=line.product_id and line.product_id.id or False,
                qty=0.0,
                uom=False,
                qty_uos=0.0,
                uos=False,
                name='',
                partner_id=self.partner_id.id,
                lang=False,
                update_tax=True,
                date_order=False,
                packaging=False,
                fiscal_position=self.fiscal_position.id,
                flag=False)
            vals['value']['discount'] = line.discount
            vals['value']['product_id'] = (line.product_id and
                                           line.product_id.id or False)
            vals['value']['state'] = 'draft'
            vals['value']['product_uom_qty'] = line.product_uom_qty
            vals['value']['product_uom'] = (line.product_uom and
                                            line.product_uom.id or False)
            lines.append(vals['value'])
        self.order_line = lines
        if not self.template_id.note:
            self.template_id.note = ''
        self.note = self.merge_message(self.template_id.note,
                                       self.template_id.id)

    @api.multi
    def merge_message(self, note, template):

        if self._context is None:
            self._context = {}

        def merge(match):
            exp = str(match.group()[2:-2]).strip()
            result = None
            try:
                result = eval(exp,
                              {'object': template,
                               'context': dict(self._context),
                               'time': time,
                               })
            except:
                raise Warning(_('Error!'),
                              _("""Wrong python condition defined for
                              template: %s.""") % (template.name))
            if result in (None, False):
                return str("--------")
            return tools.ustr(result)

        com = re.compile(r'(\[\[.+?\]\])')
        message = com.sub(merge, note)

        return message

sale_order()