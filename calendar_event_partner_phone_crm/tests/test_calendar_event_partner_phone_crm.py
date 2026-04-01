# Copyright 2025 Ángel Rivas <angel.rivas@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo.tests.common import TransactionCase


class TestCalendarEventPartnerPhoneCrm(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        cls.partner = cls.env["res.partner"].create(
            {
                "name": "Test Partner",
                "phone": "123456789",
                "mobile": "987654321",
            }
        )

    def test_meeting_action_sets_partner_fields(self):
        phonecall = self.env["crm.phonecall"].create(
            {
                "name": "Test Call",
                "partner_id": self.partner.id,
            }
        )

        res = phonecall.action_make_meeting()
        ctx = res["context"]

        self.assertEqual(ctx["default_principal_partner_id"], self.partner.id)
        self.assertEqual(ctx["default_principal_partner_phone"], self.partner.phone)
        self.assertEqual(ctx["default_principal_partner_mobile"], self.partner.mobile)
