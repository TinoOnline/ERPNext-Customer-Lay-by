import frappe
import unittest
from customer_layby.patches.v1.virtual_check_migration import execute

class testUpdateCustomerLayBy(unittest.TestCase):
    
    def setUp(self):
        self.create_test_customers()
        
    def create_test_customers(self):
        # Creating migration test for Verification type: ID - valid, Passport - valid and None
        customers = [
            {
                "doctype": "Customer",
                "customer_name": "Customer 1",
                "custom_verification_type": "ID",
                "custom_id_number": "9512113245186",
                "mobile_no": "0123456789",
                "custom_layby_eligible": False
            },
            {
                "doctype": "Customer",
                "customer_name": "Customer 2",
                "custom_verification_type": "Passport",
                "custom_passport_number": "A1234567",
                "custom_passport_country": "South Africa",
                "mobile_no": "0987654321",
                "custom_layby_eligible": False
            },
            {
                "doctype": "Customer",
                "customer_name": "Customer 3",
                "custom_verification_type": "None",
                "custom_id_number": None,
                "mobile_no": "1234567890",
                "custom_layby_eligible": False
            }
        ]
        
        for customer in customers:
                if not frappe.db.exists("Customer", {"customer_name": customer["customer_name"]}):
                    frappe.get_doc(customer).insert()
                
    def test_update_customer_lay_by(self):
        execute()

        customer1 = frappe.get_doc("Customer", {"customer_name": "Customer 1"})
        customer2 = frappe.get_doc("Customer", {"customer_name": "Customer 2"})
        customer3 = frappe.get_doc("Customer", {"customer_name": "Customer 3"})

        self.assertTrue(customer1.custom_layby_eligible)
        self.assertTrue(customer2.custom_layby_eligible)
        self.assertFalse(customer3.custom_layby_eligible)

    def tearDown(self):
        frappe.db.delete("Customer", {"customer_name": ["in", ["Customer 1", "Customer 2", "Customer 3"]]})
        frappe.db.commit()
        pass

if __name__ == '__main__':
    unittest.main()
    pass