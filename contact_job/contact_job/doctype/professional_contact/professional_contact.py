# Copyright (c) 2025, Adham_Hebeish and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
 
 
class ProfessionalContact(Document):
	def before_save(self):
		self.full_name = f"{self.salutation + " " if self.salutation != "None" else ""}{self.first_name} {self.middle_name + " " if self.middle_name.strip() != "" else ""}{self.last_name}"