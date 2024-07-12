app_name = "customer_layby"
app_title = "Customer Layby"
app_publisher = "Tinotenda Kurimwi"
app_description = "Lay-by functionality extension for the customer doctype"
app_email = "tinokurimwi@gmail.com"
app_license = "mit"

# include js in doctype views

doctype_js = {
    "Customer": "public/js/custom_customer_script.js"
}


# DocType Class
# ---------------
# Extend standard doctype classes

override_doctype_class = {
	"Customer": "customer_layby.customer_layby.custom_customer_layby.CustomCustomer"
}
