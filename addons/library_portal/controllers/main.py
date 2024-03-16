import json

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

class MainJSON(http.Controller):
    @http.route(
        "/library/catalog/json",
        auth="public",
        website=False
    )
    def catalog(self, **kwargs):
        book = http.request.env["library.book"]
        books = book.sudo().search([])

        # Convert books to a list of dictionaries
        books_data = []
        for book in books:
            books_data.append({
                'id': book.id,
                'name': book.name,
                # Add other fields as needed
            })

        # Convert the dictionary to a JSON string
        response_json = json.dumps({"books": books_data})

        # Return the JSON response
        return http.Response(
            response_json,
            content_type='application/json;charset=utf-8'
        )