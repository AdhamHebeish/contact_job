const login = Vue.createApp({
    data() {
        return {
            email: "",
            password: "",
            errtext: "",
        }
    },
    methods: {
        async login() {
            if (this.email.trim() == "") {
                this.errtext = "Please provide an email"
            } else if (this.password.trim() == "") {
                this.errtext = "Please provide a password"
            } else {
                try{
                    const result = await frappe.call({
                    method: "contact_job.api.auth.login",
                    type: "GET",
                    args: {
                        email: this.email,
                        password: this.password
                    }
                    });
                    if (result.message.loggedin == true) {
                            window.location.pathname = "/admin_panel";
                    } else {
                            this.errtext = "Incorrect Username or Password";
                    }
                } catch (err) {
                    console.error("An unexpected error occured: " + err)
                }
            }
        }
    }
})

login.mount("#login");