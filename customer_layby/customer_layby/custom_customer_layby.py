from erpnext.selling.doctype.customer.customer import Customer as ERPNextCustomer
import frappe

class CustomCustomer(ERPNextCustomer):
    def validate(self):
        super().validate()
        # The validation ensures that only when ID or Passport is selected, should the validation execute
        if self.custom_verification_type == "ID":
            if not self.custom_id_number:
                frappe.throw("ID Number is required if Identification Type is ID")
            if (self.custom_id_number and len(self.custom_id_number) != 13):
                frappe.throw(f'The ID number provide is not valid')
            if not self.mobile_no or (self.mobile_no and len(self.mobile_no) < 10):
                frappe.throw('The primary phone number provided is not valid')
        elif self.custom_verification_type == "Passport":
            if (not self.custom_passport_number or not self.custom_passport_country):
                frappe.throw("Passport Number and Passport Country are required if Identification Type is Passport")
            if not self.mobile_no or (self.mobile_no and len(self.mobile_no) < 10):
                frappe.throw('The primary phone number provided is not valid')