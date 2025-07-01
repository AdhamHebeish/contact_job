const new_contact_form = Vue.createApp({
    data() {
        return {
            code: 0,
            firstname: "",
            middlename: "",
            lastname: "",
            email: "",
            phone: "",
            salutation: "None",
            designation: "",
            gender: "",
            address: "",
            companyname: "",
            title: "",
            industry: "",
            experience: 0,
            degree: "None",
            employed: false,
            looking_job: false,
            listsalute: [
                "None",
                "Prof",
                "Master",
                "Miss",
                "Sir",
                "Madam",
                "Mrs",
                "Dr",
                "Mx",
                "Ms",
                "Mr"
            ],
            listgender: [
                "Male",
                "Female",
                "Prefer not to Say",
                "Other"
            ],
            listindustry: [
                "Procurement",
                "Healthcare",
                "Pharmaceutical",
                "Education",
                "Services",
                "Industry",
                "Retail",
                "Infrastructure",
                "Governmental",
                "Utilities",
                "Telecommunications",
                "Military",
                "R&D",
                "Finance",
                "Commerce",
                "Security",
                "Manufacturing",
                "Transport",
                "Insurance",
                "Advertising",
                "Marketing",
                "Other"
            ],
            listdegree: [
                "None",
                "Primary school",
                "Secondary school",
                "High school",
                "Associate degree",
                "Bachelor degree",
                "Master Degree",
                "Doctor of Philosophy"
            ]
        }
    },
    methods: {
        async validatecontact() {
            if (!this.firstname || !this.lastname || !this.gender || !this.title || !this.industry ) {
                frappe.msgprint(
                    msg="Please fill out the required fields marked by an Asterik*",
                    title="Required Fields Empty"
                );
                return
            } else if (this.phone != "" || this.email != "") {
                const response = frappe.call({
                    method: "contact_job.api.doctype.validateinfo",
                    type: "GET",
                    args: {
                        email: this.email,
                        phone: this.phone
                    }
                });
                if (response.message.email == "" && !response.message.phone) {
                    frappe.msgprint(
                    msg="The email and mobile number are invalid",
                    title="Invalid Fields"
                )
                } else if (response.message.email == "") {
                    frappe.msgprint(
                    msg="This email is invalid",
                    title="Invalid Field"
                )
                } else if (!response.message.phone) {
                    frappe.msgprint(
                    msg="This mobile number is invalid",
                    title="Invalid Field"
                )
                } else {
                    this.submitcontact()
                }
            } else {
                this.submitcontact()
            }
        },
        async submitcontact() {
            const result = await frappe.call({
                method: "contact_job.api.doctype.new_contact",
                type: "GET",
                args: {
                    first_name: this.firstname,
                    middle_name: this.middlename,
                    last_name: this.lastname,
                    email: this.email,
                    address: this.address,
                    salutation: this.salutation,
                    designation: this.designation,
                    gender: this.gender,
                    mobile_no: this.phone,
                    company_name: this.companyname,
                    job_title: this.title,
                    industry: this.industry,
                    exp: this.experience,
                    education: this.degree,
                    employed: this.employed,
                    looking: this.looking_job
                }
            });
            this.code = result.message.code
            if (this.code == 400) {
                frappe.throw(
                    msg=result.message.msg,
                    title="An error occured"
                )
            } else if (this.code == 404) {
                frappe.throw(
                    msg="Your Contact has not been saved properly. Please try again.",
                    title="An error has occured during saving"
                )
            }
        }
    }
})

new_contact_form.mount("#new_contact");