# -*- coding: utf-8 -*-

from openerp.osv import osv, fields
from openerp.tools.translate import _
import logging

class product_template(osv.osv):
    _inherit = "product.template"

    def _get_attached_docs(self, cr, uid, ids, field_name, arg, context):
        res = {}
        attachment = self.pool.get('ir.attachment')
        for id in ids:
            product_attachments = attachment.search(cr, uid, [('res_model', '=', 'product.template'), ('res_id', '=', id)], context=context, count=True)
            res[id] = product_attachments or 0
        return res


    _columns = {
        'doc_count': fields.function(
            _get_attached_docs, string="Number of documents attached", type='integer'
        )
    }

    def attachment_tree_view(self, cr, uid, ids, context):
        domain = [
             '&', ('res_model', '=', 'product.template'), ('res_id', 'in', ids),
        ]
        res_id = ids and ids[0] or False
        return {
            'name': _('Attachments'),
            'domain': domain,
            'res_model': 'ir.attachment',
            'type': 'ir.actions.act_window',
            'view_id': False,
            'view_mode': 'kanban,tree,form',
            'view_type': 'form',
            'limit': 80,
            'context': "{'default_res_model': '%s','default_res_id': %d}" % (self._name, res_id)
        }
