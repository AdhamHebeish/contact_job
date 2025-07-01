import frappe
from frappe.utils import validate_email_address, validate_phone_number
from frappe.query_builder import Order

@frappe.whitelist(allow_guest=True)
def new_contact(
        first_name,
        middle_name,
        last_name,
        email,
        address,
        salutation,
        designation,
        gender,
        mobile_no,
        company_name,
        job_title,
        industry,
        exp:int,
        education,
        employed:bool,
        looking:bool
    ):
    try:
        doc = frappe.new_doc('Professional Contact')
        doc.first_name = str(first_name)
        doc.middle_name = str(middle_name)
        doc.last_name = str(last_name)
        doc.email = str(email)
        doc.address = str(address)
        doc.salutation = str(salutation)
        doc.designation = str(designation)
        doc.gender = str(gender)
        doc.mobile_no = str(mobile_no)
        doc.company_name = str(company_name)
        doc.job_title = str(job_title)
        doc.industry = str(industry)
        doc.years_of_experience = int(exp)
        doc.education_level = str(education)
        if employed == True:
            doc.employed = 1
        else:
            doc.employed = 0
        if looking == True:
            doc.is_looking_for_job = 1
        else:
            doc.is_looking_for_job = 0
        try:
            doc.insert(ignore_permissions=True)
            frappe.db.commit()
        except Exception as e:
            response = {
            "code": 400,
            "msg": f"An unexpected error occured while saving your contact: {e}"
            }
            return response
    except Exception as e:
        response = {
            "code": 400,
            "msg": f"An unexpected error occured while saving your contact: {e}"
        }
        return response
    if frappe.db.exists("Professional Contact", {"first_name": first_name,"last_name": last_name}):
        response = {
            "code": 200,
            "msg": "OK"
        }
        return response
    else:
        response = {
            "code": 404,
            "msg": "Not Found"
            }
        return response
    
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
    contacts = frappe.qb.DocType("Professional Contact")
    query = (
        frappe.qb.from_(contacts)
        .select(
            contacts.full_name,
            contacts.creation,
            contacts.first_name,
            contacts.middle_name,
            contacts.last_name,
            contacts.email,
            contacts.address,
            contacts.salutation,
            contacts.designation,
            contacts.gender,
            contacts.mobile_no,
            contacts.company_name,
            contacts.job_title,
            contacts.industry,
            contacts.years_of_experience,
            contacts.education_level,
            contacts.employed,
            contacts.is_looking_for_job
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