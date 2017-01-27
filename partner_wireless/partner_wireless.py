# -*- coding: utf-8 -*-
##############################################################################
#
#    This module uses OpenERP, Open Source Management Solution Framework.
#    Copyright (C) 2014-Today BRUDER Datentechnik (<http://www.bruder-datentechnik.de>)
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

from openerp import tools
from openerp.osv import osv
from openerp.osv import fields


class res_partner(osv.osv):
    _inherit = "res.partner"
    _columns = {
        'router_type': fields.char('Router'),
        'router_pass': fields.char('Router Password'),
        'wireless_ssid': fields.char('Wireless SSID'),
        'wireless_security': fields.char('Wireless Security'),
        'wireless_key': fields.char('Wireless Key'),
    }

    _defaults = {
    }