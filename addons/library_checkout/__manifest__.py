{
    "name": "Library Book Checkout",
    "version": "16.0.1.0.0",
    "summary": "Members can borrow books from the library.",
    "depends": [
        "library_member",
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
        "security/ir.model.access.csv",

        "wizard/checkout_mass_message_wizard_view.xml",

        "views/library_menu.xml",

        "views/checkout_view.xml",
        "views/checkout_kanban_view.xml",

        "data/library_checkout_stage.xml",
    ],
    "assets": {
        "web.assets_backend": {
            "library_checkout/static/src/css/checkout.css",
            "library_checkout/static/src/js/checkout.js",
        }
    }

}
