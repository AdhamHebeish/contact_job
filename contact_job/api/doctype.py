import frappe
from frappe.utils import validate_email_address, validate_phone_number
from frappe.query_builder import Order

@frappe.whitelist(allow_guest=True)
def validateinfo(email, phone):
    emailvalid = validate_email_address(email, throw=False)
    phonevalid = validate_phone_number(phone, throw=False)
    response = {
        "email": emailvalid,
        "phone": phonevalid
    }
    return response  

@frappe.whitelist(allow_guest=True)
def get_contacts():
    contacts = frappe.qb.DocType("Contact")
    query = (
        frappe.qb.from_(contacts)
        .select(
            contacts.full_name,
            contacts.creation,
            contacts.first_name,
            contacts.middle_name,
            contacts.last_name,
            contacts.custom_email,
            contacts.custom_custom_address,
            contacts.custom_custom_salutation,
            contacts.designation,
            contacts.gender,
            contacts.custom_custom_phone,
            contacts.company_name,
            contacts.custom_job_title,
            contacts.custom_industry,
            contacts.custom_years_of_experience,
            contacts.custom_education_level,
            contacts.custom_employed,
            contacts.custom_is_looking_for_job
        )
        .orderby(contacts.creation, order=Order.desc)
    )
    response = query.run(as_dict=True)
    return response

@frappe.whitelist(allow_guest=True)
def new_apply(uname,email,cname,cmail,title):
    doc = frappe.new_doc("Admin Application")
    doc.username = str(uname)
    doc.email = str(email)
    doc.company = str(cname)
    doc.company_email = str(cmail)
    doc.title = str(title)
    doc.approval = "Open"
    try:
        doc.insert(ignore_permissions=True)
        frappe.db.commit()
    except Exception as e:
        response = {
            "code": 400,
            "msg": f"An unexpcted error occured: {e}"
        }
        return response
    response = {
        "code": 200,
        "msg": "OK"
    }
    return response     

@frappe.whitelist(allow_guest=True)
def get_apply():
    apply = frappe.qb.DocType("Admin Application")
    query = (
        frappe.qb.from_(apply)
        .select(
            apply.creation,
            apply.username,
            apply.email,
            apply.company,
            apply.company_email,
            apply.title,
            apply.approval
        )
        .orderby(apply.creation, order=Order.desc)
    )
    response = query.run(as_dict=True)
    return response

@frappe.whitelist(allow_guest=True)
def accept_admin(email):
    try:
        if frappe.db.exists("Admin Application", {"email": email}):
            apply = frappe.get_doc("Admin Application", {"email": email})
        admin = frappe.new_doc("Site Admin")
        admin.username = str(apply.username)
        admin.email = str(apply.email)
        admin.new_password = "placeholder"
        admin.insert(ignore_permissions=True)
        apply.approval = "Accepted"
        apply.save(ignore_permissions=True)
        frappe.db.commit()
    except Exception as e:
        response = {
            "code": 400,
            "msg": f"An unexpcted error occured: {e}"
        }
        return response
    response = {
        "code": 200,
        "msg": "OK"
    }
    return response

@frappe.whitelist(allow_guest=True)
def reject_admin(email):
    try:
        if frappe.db.exists("Admin Application", {"email": email}):
            apply = frappe.get_doc("Admin Application", {"email": email})
        apply.approval = "Rejected"
        apply.save(ignore_permissions=True)
        frappe.db.commit()
    except Exception as e:
        response = {
            "code": 400,
            "msg": f"An unexpcted error occured: {e}"
        }
        return response
    response = {
        "code": 200,
        "msg": "OK"
    }
    return response