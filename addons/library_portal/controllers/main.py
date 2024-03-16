from odoo import http


class Main(http.Controller):
    @http.route(
        "/library/catalog",
        auth="public",
        website=True
    )
    def catalog(self, **kwargs):
        book = http.request.env["library.book"]
        books = book.sudo().search([])

        return http.request.render(
            "library_portal.book_catalog",
            {"books": books},
        )