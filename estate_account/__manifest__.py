# -*- coding: utf-8 -*-
{
'name': "Estate Application",
'description': """
 Link module in chapter 14 Odoo Documentation""",
'author': "Linh Thuy",
'version': '0.1',
'depends': ['estate','account'],
'data': [
    'views/estate_property_views.xml'
],
'sequence': 1,
'installable': True,
'application': True
}
