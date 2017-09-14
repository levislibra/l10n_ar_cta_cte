# -*- coding: utf-8 -*-
{
    'name': "l10n_ar_cta_cte",

    'summary': """
        Muestra de una forma bonita la cuenta corriente del cliente/proveedor.
        """,

    'description': """
        Muestra de una forma bonita la cuenta corriente del cliente/proveedor.
    """,

    'author': "LIBRASOFT",
    'website': "http://libra-soft.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'finance',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'account_accountant'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}