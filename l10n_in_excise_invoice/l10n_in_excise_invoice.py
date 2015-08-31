# -*- coding: utf-8 -*-
###########################################################################
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

from openerp import models, fields, api

class res_company(models.Model):
    _inherit = 'res.company'

    range = fields.Char(string='Range', size=64)
    division = fields.Char(string='Division', size=64)
    commissionerate = fields.Char(string='Commissionerate', size=64)
    tariff_rate = fields.Integer(string='Tariff Rate')

res_company()

class res_partner(models.Model):
    _inherit = "res.partner"

    ecc_no = fields.Char(string='ECC', size=32, help="Excise Control Code")

res_partner()

