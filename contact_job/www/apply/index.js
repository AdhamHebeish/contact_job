const app = Vue.createApp({
    data () {
        return {
            username: "",
            email: "",
            companyname: "",
            companymail: "",
            jobtitle: "",
            code: 0
        }
    },
    methods: {
        async adminapply() {
            if (!this.username || !this.email || !this.companyname || !this.companymail || !this.jobtitle) {
                frappe.msgprint(
                    msg="Please fill out all the fields",
                    title="Required Fields Empty"
                );
            } else {
                const valids = {
                    admin: await frappe.call({
                        method: "contact_job.api.doctype.validateinfo",
                        type: "GET",
                        args: {email:this.email,phone:null}
                    }),
                    company: await frappe.call({
                        method: "contact_job.api.doctype.validateinfo",
                        type: "GET",
                        args: {email:this.companymail,phone:null}
                    })
                }
                if (valids.admin.message.email == "") {
                    frappe.msgprint(
                    msg="Administrator e-mail is invalid",
                    title="Invalid Email(s)"
                    );
                } else if (valids.company.message.email == "") {
                    frappe.msgprint(
                    msg="Company e-mail is invalid",
                    title="Invalid Email(s)"
                    );
                } else {
                    this.newapply();
                }
            }
        },
        async newapply() {
            const confirm = await frappe.call({
                method: "contact_job.api.doctype.new_apply",
                type: "GET",
                args: {
                    uname: this.username,
                    email: this.email,
                    cname: this.companyname,
                    cmail: this.companymail,
                    title: this.jobtitle
                }
            });
            this.code = confirm.message.code
            if (this.code == 400) {
                frappe.msgprint(
                    msg=confirm.message.msg,
                    title="An error occured"
                )
            }
        }
    }
})

app.mount("#apply")