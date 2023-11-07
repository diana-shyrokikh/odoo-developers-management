from odoo import api, fields, models


class Developer(models.Model):
    _name = "developers_management.developer"
    _inherit = [
        "mail.thread",
        "mail.activity.mixin",
    ]
    _description = "Developer"
    _rec_name = "name"

    GENDERS = [
        ("male", "Male"),
        ("female", "Female")
    ]
    TYPES = [
        ("front-end", "Front-end"),
        ("back-end", "Back-end"),
        ("full-stack", "Full-stack"),
        ("designer", "Designer"),
        ("out-stuff", "Out-stuff"),
    ]

    name = fields.Char(
        string="Name",
        tracking=True,
        required=True,
    )
    type = fields.Selection(
        TYPES,
        string="Type",
        tracking=True,
        required=True
    )
    global_identification = fields.Char(
        compute="_compute_global_identification",
        store=True,
        tracking=True,
        string="Global Identification",
    )
    phone = fields.Char(
        string="Phone Number",
        tracking=True,
    )
    email= fields.Char(
        string="Email",
        required=True,
        tracking=True,
    )
    date_of_birth = fields.Date(
        string="Date of Birth",
        tracking=True,
    )
    address = fields.Text(
        string="Address",
        tracking=True,
    )
    gender = fields.Selection(
        GENDERS,
        string="Gender",
        tracking=True
    )
    active = fields.Boolean(
        string="Active",
        default=True,
        tracking=True,
    )
    position = fields.Char(
        string="Position",
        tracking=True,
    )
    company_id = fields.Many2one(
        comodel_name="developers_management.company",
        string="Company"
    )

    _sql_constraints = [(
        "name_uniq",
        "unique (name)",
        "The name must be unique!"
    ),]


    @api.depends("name", "type")
    def _compute_global_identification(self):
        for developer in self:
            developer.global_identification = f"{developer.name}-{developer.type}"
