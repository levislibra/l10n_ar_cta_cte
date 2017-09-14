# -*- coding: utf-8 -*-

from openerp import models, fields, api

class CtaCte(models.Model):
	_name = 'res.partner'
	_inherit = 'res.partner'

	def ver_ctacte(self, cr, uid, ids, context=None):
		partner_obj = self.pool.get('res.partner')
		partner_id = partner_obj.browse(cr, uid, ids[0], context=None)

		property_account_receivable_id = partner_id.property_account_receivable_id.id
		property_account_payable_id = partner_id.property_account_payable_id.id

		ctacte_obj = self.pool.get('account.move.line')
		ctacte_ids = ctacte_obj.search(cr, uid, [
			('partner_id', '=', partner_id.id),
			('account_id', 'in', [property_account_receivable_id, property_account_payable_id]),
			])

		model_obj = self.pool.get('ir.model.data')
		data_id = model_obj._get_id(cr, uid, 'l10n_ar_cta_cte', 'view_ctacte')
		view_id = model_obj.browse(cr, uid, data_id, context=None).res_id
		return {
			'domain': "[('id', 'in', ["+','.join(map(str, ctacte_ids))+"])]",
			'name': ('Cta Cte'),
			'view_type': 'form',
			'view_mode': 'tree',
			'res_model': 'account.move.line',
			'view_id': view_id,
			'type': 'ir.actions.act_window',
		}