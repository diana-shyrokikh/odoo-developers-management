from odoo import fields, models

class Member(models.Model):
    _name = "library.member"
    _description = "Library Member"
    # _inherits = {"res.partner": "partner_id"} the same as delegate=True

    card_number = fields.Char()
    partner_id = fields.Many2one(
        comodel_name="res.partner",
        delegate=True,
        ondelete="cascade",
        required=True
    )
