# Copyright 2025 Ángel Rivas <angel.rivas@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo import api, fields, models


class CalendarEvent(models.Model):
    _inherit = "calendar.event"

    principal_partner_id = fields.Many2one("res.partner", string="Partner")
    principal_partner_phone = fields.Char(string="Phone")
    principal_partner_mobile = fields.Char(string="Mobile")

    @api.onchange("principal_partner_id")
    def _onchange_principal_partner_id(self):
        if self.principal_partner_id:
            self.principal_partner_phone = self.principal_partner_id.phone
            self.principal_partner_mobile = self.principal_partner_id.mobile

    @api.model
    def create(self, vals):
        if vals.get("principal_partner_id"):
            partner = self.env["res.partner"].browse(vals["principal_partner_id"])
            vals["principal_partner_phone"] = partner.phone
            vals["principal_partner_mobile"] = partner.mobile
        return super().create(vals)
