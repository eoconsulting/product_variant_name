# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2012 Tiny SPRL (<http://tiny.be>)
#                            Sistemas ADHOC
#                            Mariano Ruiz (Enterprise Objects Consulting)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################


{
    'name': 'Product Variant Name',
    'version': '1.0',
    'description': """
    This module change how the product name is computed in a order line.
    If the product have variants description, use name_template + variants,
    else use name + variants.
    Without this module, when product have variants, the variant description
    is added twice.
    """,
    'category': 'Sales Management',
    'author': 'Enterprise Objects Consulting',
    'website': 'http://www.eoconsulting.com.ar',
    'depends': ['product'],
    'init_xml': [],
    'update_xml': [],
    'demo_xml': [],
    'test':[],
    'installable': True,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
