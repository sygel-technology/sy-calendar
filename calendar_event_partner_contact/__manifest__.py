# Copyright 2025 Ángel Rivas <angel.rivas@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Calendar Event Partner Contact",
    "summary": "Adds main partner info (phone and mobile) to calendar events.",
    "version": "18.0.1.0.0",
    "category": "Calendar",
    "website": "https://github.com/sygel-technology/sy-calendar",
    "author": "Sygel",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": ["calendar"],
    "data": [
        "views/calendar_event_views.xml",
    ],
}
