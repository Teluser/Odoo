# -*- coding: utf-8 -*-
{
'name': "Pet",
'description': """
Manage pet shop application""",
'author': "Linh Thuy",
'version': '0.1',
'depends': [],
'data': [
    'security\ir.model.access.csv',
    'views\pet_views.xml',
    'views\pet_menu_views.xml',
],
'sequence': 1,
'installable': True,
'application': True
}
