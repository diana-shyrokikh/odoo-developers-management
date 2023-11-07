from odoo import api, fields, models


class Company(models.Model):
    _name = "developers_management.company"
    _inherit = [
        "mail.thread",
        "mail.activity.mixin",
    ]
    _description = "Company"
    _rec_name = "name"

    name = fields.Char(
        string="Name",
        tracking=True,
        required=True,
    )
    address = fields.Text(
        string="Address",
        tracking=True,
    )
    developers = fields.One2many(
        comodel_name="developers_management.developer",
        inverse_name="company_id",
        string="Developers",
    )
    active = fields.Boolean(
        string="Active",
        default=True,
        tracking=True,
    )
    _sql_constraints = [(
        "name_uniq",
        "unique (name)",
        "The name must be unique!"
    ),]
