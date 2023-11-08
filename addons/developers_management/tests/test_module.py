from odoo.tests import common


class TestDeveloperCompany(common.TransactionCase):
    def setUp(self):
        super(TestDeveloperCompany, self).setUp()
        self.Developer = self.env["developers_management.developer"]
        self.Company = self.env["developers_management.company"]

        self.developer = self.Developer.create({
            "name": "John Jonenko",
            "type": "back-end",
            "email": "john@example.com",
            "gender": "male",
            "active": True,
        })

        self.company = self.Company.create({
            "name": "ABC Inc.",
            "address": "123 Main St, City",
            "active": True
        })

    def test_developer_creation(self):
        self.assertEqual(self.developer.name, "John Jonenko")
        self.assertEqual(self.developer.email, "john@example.com")

    def test_developer_edition(self):
        self.developer.write({
            "name": "Anna Annanenko",
            "type": "front-end",
            "email": "anna@example.com",
            "gender": "female",
            "active": False,
        })
        self.assertEqual(self.developer.name, "Anna Annanenko")
        self.assertEqual(self.developer.type, "front-end")
        self.assertEqual(self.developer.gender, "female")
        self.assertFalse(self.developer.active)
        self.assertEqual(self.developer.email, "anna@example.com")

    def test_developer_add_company(self):
        self.developer.write({
            "company_id": self.company.id,
        })

        self.assertEqual(self.developer.company_id.id, self.company.id)

    def test_company_creation(self):
        self.assertEqual(self.company.name, "ABC Inc.")
        self.assertEqual(self.company.address, "123 Main St, City")

    def test_company_edition(self):
        self.company.write({
            "name": "ABCD Inc.",
        })

        self.assertEqual(self.company.name, "ABCD Inc.")

    def test_company_add_developer(self):
        developer = self.Developer.create({
            "name": "Pavlo Pavlenko",
            "type": "back-end",
            "email": "pavlo@example.com",
            "gender": "male",
        })

        self.company.write({"developers": [(4, developer.id)]})
        self.assertTrue(developer in self.company.developers)
