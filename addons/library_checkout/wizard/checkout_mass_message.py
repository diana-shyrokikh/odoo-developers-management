from odoo import api, exceptions, fields, models


class CheckoutMassMessage(models.TransientModel):
    _name = "library.checkout.massmessage"
    _description = "Send Message to Borrowers"

    checkout_ids = fields.Many2many(
        "library.checkout",
        string="Checkouts",
    )
    message_subject = fields.Char()
    message_body = fields.Html()

    @api.model
    def default_get(self, field_names):
        defaults_dict = super().default_get(field_names)
        checkout_ids = self.env.context["active_ids"]
        print("checkout_ids", checkout_ids)
        defaults_dict["checkout_ids"] = self.env["library.checkout"].browse(checkout_ids)
        print("defaults_dict", defaults_dict)
        # Add values to the defaults_dict here
        return defaults_dict


    def button_send(self):
        self.ensure_one()
        for checkout in self.checkout_ids:
            checkout.message_post(
                body=self.message_body,
                subject=self.message_subject,
                subtype_xmlid='mail.mt_comment',
            )
        return True