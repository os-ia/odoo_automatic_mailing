# -*- encoding: utf-8 -*-

from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    # The option to select thw way of send notifications (email or post)
    os_invoice_send_option = fields.Selection([
        ('email', "Email"),
        ('post', "Post")], string='Invoice Channel', required=True, default='email',
        help="Set preference notification type for invoices.")