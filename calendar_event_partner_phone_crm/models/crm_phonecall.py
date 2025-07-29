# Copyright 2025 Ángel Rivas <angel.rivas@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models


class CRMPhonecall(models.Model):
    _inherit = "crm.phonecall"

    def action_make_meeting(self):
        res = super().action_make_meeting()
        res["context"]["default_principal_partner_id"] = self.partner_id.id
        res["context"]["default_principal_partner_phone"] = self.partner_id.phone
        res["context"]["default_principal_partner_mobile"] = self.partner_id.mobile
        return res
