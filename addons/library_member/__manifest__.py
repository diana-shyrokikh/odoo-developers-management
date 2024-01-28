{
    "name": "Library Members",
    "version": "16.0.1.0.0",
    "summary": "Manage members borrowing books.",
    "depends": [
        "library_app",
        "mail"
    ],
    "license": "AGPL-3",
    "application": False,
    "sequence": -199,
    "author": "Diana Shyrokikh",
    "website": "https://github.com/PacktPublishing"
               "/Odoo-15-Development-Essentials",
    "category": "Services/Library",
    "data": [
        "security/library_security.xml",
        "security/ir.model.access.csv",

        "views/book_view.xml",
        "views/member_view.xml",

        "views/library_menu.xml",
    ],
}
