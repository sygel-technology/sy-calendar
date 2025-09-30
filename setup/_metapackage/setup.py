import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo-addons-sygel-technology-sy-calendar",
    description="Meta package for sygel-technology-sy-calendar Odoo addons",
    version=version,
    install_requires=[
        'odoo-addon-calendar_activity_event_done>=15.0dev,<15.1dev',
        'odoo-addon-calendar_document_popup>=15.0dev,<15.1dev',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 15.0',
    ]
)
