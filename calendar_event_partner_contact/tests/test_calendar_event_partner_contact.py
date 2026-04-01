# Copyright 2025 Ángel Rivas <angel.rivas@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo.tests.common import TransactionCase


class TestCalendarEventPartnerContact(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        cls.partner = cls.env["res.partner"].create(
            {
                "name": "Partner Test",
                "phone": "987654321",
                "mobile": "600100200",
            }
        )

    def test_onchange_principal_partner_id(self):
        partner_id = self.partner.id
        event = self.env["calendar.event"].new(
            {
                "principal_partner_id": partner_id,
            }
        )
        event._onchange_principal_partner_id()
        self.assertEqual(event.principal_partner_phone, self.partner.phone)
        self.assertEqual(event.principal_partner_mobile, self.partner.mobile)

    def test_create_event_with_principal_partner(self):
        event = self.env["calendar.event"].create(
            {
                "name": "Test Event",
                "principal_partner_id": self.partner.id,
            }
        )
        self.assertEqual(event.principal_partner_phone, self.partner.phone)
        self.assertEqual(event.principal_partner_mobile, self.partner.mobile)
