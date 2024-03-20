# -*- coding: utf-8 -*- 


{
    'name': 'Picking delivery slip by product',
    'author': 'Soft-integration',
    'application': False,
    'installable': True,
    'auto_install': False,
    'qweb': [],
    'description': False,
    'images': [],
    'version': '1.0.1.1',
    'category': 'Inventory/Inventory',
    'demo': [],
    'depends': ['stock'],
    'data': [
        'report/stock_report_views.xml',
        'report/report_deliveryslip_by_product.xml'
    ],
    'license': 'LGPL-3',
}
