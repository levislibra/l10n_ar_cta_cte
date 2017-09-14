# -*- coding: utf-8 -*-

from openerp import models, fields, api

class CtaCte(models.Model):
	_name = 'res.partner'
	_inherit = 'res.partner'

	def ver_ctacte(self, cr, uid, ids, context=None):
		ctacte_obj = self.pool.get('account.move.line')
		ctacte_ids = ctacte_obj.search(cr, uid, [])

		model_obj = self.pool.get('ir.model.data')
		data_id = model_obj._get_id(cr, uid, 'l10n_ar_cta_cte', 'view_ctacte')
		print data_id
		view_id = model_obj.browse(cr, uid, data_id, context=None).res_id
		print view_id
		return {
			'domain': "[('id', 'in', ["+','.join(map(str, ctacte_ids))+"])]",
			'name': ('Cta Cte'),
			'view_type': 'form',
			'view_mode': 'tree',
			'res_model': 'account.move.line',
			'view_id': 12802,
			'type': 'ir.actions.act_window',
		}