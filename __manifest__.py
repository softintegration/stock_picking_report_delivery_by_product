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
    'version': '1.0.1',
    'category': 'Inventory/Inventory',
    'demo': [],
    'depends': ['stock'],
    'data': [
        #'data/report_paperformat_data.xml',
        #'data/stock_quant_package_report_custom_formats_data.xml',
        #'report/report_package_barcode.xml',
        'report/stock_report_views.xml',
        'report/report_deliveryslip_by_product.xml'
    ],
    'license': 'LGPL-3',
}
