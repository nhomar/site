# -*- coding: utf-8 -*-
{
    'name': "PyVe Site",

    'summary': """
        Pyve initializator
    """,

    'author': "Python Venezuela",

    'website': "http://www.python.org.ve",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Administration',

    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'website_blog',
        'website_event',
        'website_forum_doc',
        'website_twitter',
        'membership',
        'auth_oauth',
        'auth_openid',
    ],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'templates.xml',
    ],

    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}