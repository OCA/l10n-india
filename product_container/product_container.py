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

from openerp import models, fields


class product_ul(models.Model):
    _inherit = "product.ul"

    container_id = fields.Many2one('product.template', 'Container Product',
                                   domain=[('container_ok', '=', True)])
product_ul()


class product_product(models.Model):
    _inherit = 'product.template'

    container_ok = fields.Boolean(string='Container',
                                  help="""Select this if the product will act
                                   as a container to carry other products.""")
    container_id = fields.Many2one('product.template', 'Packed In',
                                   domain=[('container_ok', '=', True)])

product_product()