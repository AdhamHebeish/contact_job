const view_contact = Vue.createApp({
    delimiters: [ "[[" , "]]" ],
    data () {
        return {
            contacts: [],
            industry: "Any",
            employed: "Any",
            looking: "Any"
        }
    },
    methods: {
        async get_contacts() {
            const data = await frappe.call({
                method: "contact_job.api.doctype.get_contacts",
                type: "GET"
            });
            for (let i in data.message) {
                const obj = data.message[i]
                let person = {
                    title: obj.full_name,
                    fname: obj.first_name,
                    mname: null,
                    lname: obj.last_name,
                    mail: null,
                    address: null,
                    salute: obj.salutation,
                    design: null,
                    gender: obj.gender,
                    mobile: null,
                    company: null,
                    job: obj.job_title,
                    industry: obj.industry,
                    exp: obj.years_of_experience,
                    degree: obj.education_level,
                    employed: Boolean(obj.employed),
                    looking: Boolean(obj.is_looking_for_job),
                    min: true,
                    new: false
                }
                if (obj.middle_name) {
                    person.mname = obj.middle_name
                }
                if (obj.email) {
                    person.mail = obj.email
                }
                if (obj.address) {
                    person.address = obj.address
                }
                if (obj.designation) {
                    person.design = obj.designation
                }
                if (obj.mobile_no) {
                    person.mobile = obj.mobile_no
                }
                if (obj.company_name) {
                    person.company = obj.company_name
                }
                const lastweek = new Date()
                lastweek.setDate(lastweek.getDate() - 7)
                const added = new Date(obj.creation)
                if (added >= lastweek) {
                    person.new = !person.new
                }
                this.contacts.push(person);
            }
        }
    },
    mounted() {
        this.get_contacts();
    }
})

view_contact.mount("#view")