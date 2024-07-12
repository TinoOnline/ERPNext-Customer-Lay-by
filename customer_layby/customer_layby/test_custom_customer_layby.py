import unittest
import frappe
from customer_layby.customer_layby.custom_customer_layby import CustomCustomer
from erpnext.selling.doctype.customer.customer import Customer as ERPNextCustomer

class TestCustomCustomer(unittest.TestCase):
    
    # The structure of the tests is testing for exceptions, since that would be the only cases where the input isn't valid

    def setUp(self):
        self.customer_data = {
            "doctype": "Customer",
            "customer_name": "Test Customer",
            "customer_type": "Individual",
            "custom_verification_type": "ID",
            "custom_id_number": "1234567890123",
            "mobile_no": "0123456789"
        }
        
        
        if not frappe.db.exists("Customer", {"customer_name": "Test Customer"}):
            frappe.get_doc(self.customer_data).insert()
        
                   
    def test_invalid_id_length(self):
        self.customer_data["custom_id_number"] = "123456"
        custom_customer = frappe.get_doc(self.customer_data)
        with self.assertRaises(frappe.exceptions.ValidationError):
            custom_customer.validate()

    def test_missing_id(self):
        self.customer_data["custom_id_number"] = None
        custom_customer = frappe.get_doc(self.customer_data)
        with self.assertRaises(frappe.exceptions.ValidationError):
            custom_customer.validate()

    def test_invalid_mobile_length(self):
        self.customer_data["mobile_no"] = "123456"
        custom_customer = frappe.get_doc(self.customer_data)
        with self.assertRaises(frappe.exceptions.ValidationError):
            custom_customer.validate()
            

    def test_missing_passport_details(self):
        self.customer_data["custom_verification_type"] = "Passport"
        self.customer_data["custom_passport_number"] = None
        self.customer_data["custom_passport_country"] = None
        custom_customer = frappe.get_doc(self.customer_data)
        with self.assertRaises(frappe.exceptions.ValidationError):
            custom_customer.validate()

    def tearDown(self):
        frappe.db.delete("Customer", {"customer_name": "Test Customer"})
        frappe.db.commit()

if __name__ == '__main__':
    unittest.main()
