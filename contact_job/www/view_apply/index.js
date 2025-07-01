const view_apply = Vue.createApp({
    delimiters: [ "[[" , "]]" ],
    data () {
        return {
            apply: [],
            status: "Any"
        }
    },
    methods: {
        async get_apply() {
            const data = await frappe.call({
                method: "contact_job.api.doctype.get_apply",
                type: "GET"
            });
            for (let i in data.message) {
                const obj = data.message[i]
                let admin = {
                    name: obj.username,
                    status: obj.approval,
                    email: obj.email,
                    cname: obj.company,
                    cmail: obj.company_email,
                    job: obj.title,
                    min: true
                }
                this.apply.push(admin)
            }
        },
        async accept_admin(admin) {
            const res = await frappe.call({
                method: "contact_job.api.doctype.accept_admin",
                type: "GET",
                args: {email:admin}
            });
            this.code = res.message.code
            if (this.code == 400) {
                frappe.msgprint(
                    msg=res.message.msg,
                    title="An error occured"
                )
            } else if (this.code == 200) {
                frappe.msgprint(
                    msg="Please Set this Administrator's Password (Password temporarily set to 'placeholder')",
                    title="Operation Successful"
                )
            }
        },
        async reject_admin(admin) {
            const res = await frappe.call({
                method: "contact_job.api.doctype.reject_admin",
                type: "GET",
                args: {email:admin}
            });
            this.code = res.message.code
            if (this.code == 400) {
                frappe.msgprint(
                    msg=res.message.msg,
                    title="An error occured"
                )
            }  else if (this.code == 200) {
                frappe.msgprint(
                    msg="Please Reload Page",
                    title="Operation Successful"
                )
            }
        }
    },
    mounted() {
        this.get_apply();
    }
})

view_apply.mount("#view_apply")