import frappe
from frappe import _

def validate_task_access(doc, method):
    user = frappe.session.user

    # Check if the user has the "Task Completer" role
    if "Task Completer" in frappe.get_roles(user):
        # Ensure the task is assigned to the user
        assigned_users = [
            d.allocated_to
            for d in frappe.get_all("ToDo", filters={"reference_type": "Task", "reference_name": doc.name}, fields=["allocated_to"])
        ]
        if user not in assigned_users:
            frappe.throw(_("You are not authorized to access this Task."))
