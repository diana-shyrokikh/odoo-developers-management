from odoo import http


class Books(http.Controller):
    @http.route("/library/books")
    def list(self, **kwargs):
        book = http.request.env["library.book"]
        books = book.search([])

        return http.request.render(
            "library_app.book_list_template",
            {"books": books}
        )
