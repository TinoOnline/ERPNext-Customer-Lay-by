import frappe

def execute():
    # Filter through all the customers and apply layby eligibility to those who qualify
    customers = frappe.get_all("Customer", filters={"disabled": 0}, fields=["name"])
    for customer in customers:
        customer_doc = frappe.get_doc("Customer", customer.name)
        customer_doc.db_set('custom_layby_eligible', check_eligibility(customer_doc))


def check_eligibility(doc):
    custom_layby_eligible = False

    if doc.custom_verification_type == 'ID':
        if doc.custom_id_number and len(doc.custom_id_number) == 13 and doc.mobile_no and len(doc.mobile_no) > 9:
            custom_layby_eligible = True
    elif doc.custom_verification_type == 'Passport':
        if doc.custom_passport_number and doc.custom_passport_country and doc.mobile_no and len(doc.mobile_no) > 9:
            custom_layby_eligible = True

    return custom_layby_eligible
