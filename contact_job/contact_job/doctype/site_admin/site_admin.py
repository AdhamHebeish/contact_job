# Copyright (c) 2025, Adham_Hebeish and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
from contact_job.api.password import update_password


class SiteAdmin(Document):
	def before_save(self):
		if self.new_password != "":
			self.password = update_password(self.new_password)
			self.new_password = ""
