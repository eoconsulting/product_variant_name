# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2013  Enterprise Objects Consulting
#
#    Author: Mariano Ruiz <mrsarm@gmail.com>
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

from osv import osv
from osv import fields

class product_product(osv.osv):
    _name = 'product.product'
    _inherit = 'product.product'

    def name_get(self, cr, user, ids, context={}):
        if not len(ids):
            return []
        def _name_get(d):
            name = d.get('name','')
            code = d.get('default_code',False)
            if code:
                name = '[%s] %s' % (code,name)
            if d.get('variants'):
                name = name + ' - %s' % (d['variants'],)
            return (d['id'], name)

        partner_id = context.get('partner_id', False)

        result = []
        for product in self.browse(cr, user, ids, context=context):
            sellers = filter(lambda x: x.name.id == partner_id, product.seller_ids)
            if sellers:
                for s in sellers:
                    mydict = {
                              'id': product.id,
                              'name': s.product_name or product.name,
                              'default_code': s.product_code or product.default_code,
                              'variants': product.variants
                              }
                    result.append(_name_get(mydict))
            else:
                name = product.name
                if product.variants:
                    name = product.product_tmpl_id.name
                mydict = {
                          'id': product.id,
                          'name': name,
                          'default_code': product.default_code,
                          'variants': product.variants
                          }
                result.append(_name_get(mydict))
        return result

    def _product_partner_ref(self, cr, uid, ids, name, arg, context={}):
        res = {}
        for p in self.browse(cr, uid, ids, context=context):
            data = self._get_partner_code_name(cr, uid, [], p, context.get('partner_id', None), context=context)
            if not data['variants']:
                data['variants'] = p.variants
            if not data['code']:
                data['code'] = p.code
            if data['variants']:
                data['name'] = p.product_tmpl_id.name
            else:
                if not data['name']:
                    data['name'] = p.name
            res[p.id] = (data['code'] and ('['+data['code']+'] ') or '') + \
                    (data['name'] or '') + (data['variants'] and (' - '+data['variants']) or '')
        return res

    def write(self, cr, uid, ids, vals, context=None):
        if 'name' in vals:
            for product in self.browse(cr, uid, ids, context=context):
                if not product.product_tmpl_id.is_multi_variants:
                    self.pool.get('product.template').write(cr, uid, [product.product_tmpl_id.id], {'name': vals['name']}, context=context)
        return super(product_product, self).write(cr, uid, ids, vals, context=context)

    def create(self, cr, uid, vals, context=None):
        product_id = super(product_product, self).create(cr, uid, vals, context=context)
        if 'name' in vals and not vals.get('is_multi_variants', False):
            product = self.browse(cr,uid,product_id,context=context)
            self.pool.get('product.template').write(cr, uid, [product.product_tmpl_id.id], {'name': vals['name']}, context=context)
        return product_id

    _columns = {
        'partner_ref' : fields.function(_product_partner_ref, type='char', string='Customer ref'),
    }
