# -*- coding: utf-8 -*-
{
'name': "Real Estate",
'description': """
Demo excercise in Odoo documentation """,
'author': "Linh Thuy",
'version': '0.1',
'category': "Real Estate/Brokerage",
'depends': ['base'],
'data': [
    'security/security.xml',
    'security/security_rules.xml',
    'security/ir.model.access.csv',
    'views/estate_property_views.xml',
    'views/estate_property_offer_views.xml',
    'views/estate_property_type_views.xml',
    'views/estate_propetty_tag_views.xml',
    'views/estate_menus.xml',
    'views/res._users_views.xml'
],
'sequence': 1,
'installable': True,
'application': True
}
