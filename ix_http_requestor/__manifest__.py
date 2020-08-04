{
    'name': 'HTTP Requestor',
    'version': '1.0.0',
    'author': 'Afwan Wali Hamim',
    'category': 'ix Module/Tools',
    'website': 'https://afwan.id/',
    'summary': 'Create HTTP request and schedule it!',
    'description': '''
    Create HTTP Request from Odoo and scheduling using
    scheduled automation of Odoo.
    ''',
    'depends': [
        'base'
    ],
    'data': [
        'security/ir.model.access.csv',
        'wizard/ix_http_request_scheduler_wiz_views.xml',
        'wizard/ix_http_request_deactivate_wiz_views.xml',
        'wizard/ix_http_test_result_wiz_views.xml',
        'views/ix_http_request_views.xml',
    ],
    'installable': True,
    'application': True
}
