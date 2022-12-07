# -*- coding: utf-8 -*-
{
    'name': "LMS",
    'version' : '1.0',
    'sequence' : 3,
    'summary': 'Library Management System',
    'description' : 'This is LMS Description',
    'author': "BJIT",
    'category': 'Uncategorized',
    'depends': ['base','hr','website','website_sale'],

    'data': [
         'security/lms_security.xml',
        'security/ir.model.access.csv',
        'views/css_loader.xml',
        'views/views.xml',
        'views/templates.xml',
        'views/books_views.xml',
        'views/awards_views.xml',
        'views/authors_views.xml',
        'views/members_views.xml',
        'views/categories_views.xml',
        'views/publishers_views.xml',
        'views/issue_books_views.xml',
        'views/create_book_isbn.xml',
        'views/member_issued_book_list.xml',
        'views/department_views.xml',
        'views/member_types_views.xml',
        'views/website_form.xml',
        # 'views/product_template.xml'
        'views/product_views.xml',
        # 'views/home_book_views.xml',
        'reports/books_report.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
