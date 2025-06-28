app_name = "contact_job"
app_title = "Contact Job"
app_publisher = "Adham_Hebeish"
app_description = "Sharing Professional Contact Information"
app_email = "app.email@contactjob.co"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "contact_job",
# 		"logo": "/assets/contact_job/logo.png",
# 		"title": "Contact Job",
# 		"route": "/contact_job",
# 		"has_permission": "contact_job.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/contact_job/css/contact_job.css"
# app_include_js = "/assets/contact_job/js/contact_job.js"

# include js, css files in header of web template
web_include_css = "/static/css/base.css"
web_include_js = "/static/js/base.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "contact_job/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "contact_job/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
home_page = "home"
base_template = "contact_job/templates/base.html"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "contact_job.utils.jinja_methods",
# 	"filters": "contact_job.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "contact_job.install.before_install"
# after_install = "contact_job.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "contact_job.uninstall.before_uninstall"
# after_uninstall = "contact_job.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "contact_job.utils.before_app_install"
# after_app_install = "contact_job.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "contact_job.utils.before_app_uninstall"
# after_app_uninstall = "contact_job.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "contact_job.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"contact_job.tasks.all"
# 	],
# 	"daily": [
# 		"contact_job.tasks.daily"
# 	],
# 	"hourly": [
# 		"contact_job.tasks.hourly"
# 	],
# 	"weekly": [
# 		"contact_job.tasks.weekly"
# 	],
# 	"monthly": [
# 		"contact_job.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "contact_job.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "contact_job.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "contact_job.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["contact_job.utils.before_request"]
# after_request = ["contact_job.utils.after_request"]

# Job Events
# ----------
# before_job = ["contact_job.utils.before_job"]
# after_job = ["contact_job.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"contact_job.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

