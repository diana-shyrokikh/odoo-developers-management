{
    "name": "Library Portal",
    "description": "Portal for library members",
    "author": "Diashiro",
    "license": "AGPL-3",
    "depends": [
        "library_checkout",
        "portal",
    ],
    "data": [
        "security/ir.model.access.csv",
        "security/library_security.xml",

        # "views/checkout_portal_templates.xml",

        "views/main_templates.xml",
    ],
    "assets": {
        "web.assets_backend": {"library_portal/static/src/css/library.css"},
    },
}