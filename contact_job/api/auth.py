import frappe
from contact_job.api.password import validate_password

@frappe.whitelist(allow_guest=True)
def login(email, password):
    if frappe.db.exists("Site Admin", {"email": email }):
        user = frappe.get_doc("Site Admin", {"email": email })
    else:
        response = {
            "code": 404,
            "loggedin": False
        }
        return response
    valid = validate_password(user,password)
    response = {
        "code": 200,
        "loggedin": valid
    }
    return response

