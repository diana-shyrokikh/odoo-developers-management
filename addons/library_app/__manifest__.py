{
    "name": "Library Management",
    "version": "16.0.1.0.0",
    "summary": "Manage library catalog and book lending",
    "depends": [
        "base",
    ],
    "license": "AGPL-3",
    "application": True,
    "sequence": -200,
    "author": "Diana Shyrokikh",
    "website": "https://github.com/PacktPublishing"
               "/Odoo-15-Development-Essentials",
    "category": "Services/Library",
    "demo": [
        "data/res.partner.csv",
        "data/library.book.csv",
        "data/book_demo.xml",
    ],
    "data": [
        "security/library_security.xml",
        "security/ir.model.access.csv",

        "views/book_view.xml",

        "views/library_menu.xml",
        "views/book_list_template.xml",

        "reports/library_book_report.xml",

    ],
}
