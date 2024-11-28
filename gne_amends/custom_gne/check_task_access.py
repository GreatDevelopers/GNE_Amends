import frappe
import json

@frappe.whitelist()
def check_task_access(task_id):
    """
    Check if the current user is authorized to view the Task document.
    """
    try:
        task = frappe.get_doc('Task', task_id)

        # Decode the JSON stored in _assign
        assigned_users = json.loads(task._assign) if task._assign else []

        # Check if the user is assigned or has the 'Project Manager' role
        if frappe.session.user in assigned_users or 'Project Manager' in frappe.get_roles():
            return True  # Authorized
        
        # Unauthorized
        return False
    
    except frappe.DoesNotExistError:
        frappe.throw(f"Task {task_id} does not exist.")
    except json.JSONDecodeError as e:
        frappe.log_error(message=str(e), title="Task Access JSON Decode Error")
        frappe.throw("An error occurred while decoding assigned users.")
    except Exception as e:
        frappe.log_error(message=str(e), title="Task Access Error")
        frappe.throw("An unexpected error occurred while checking access.")
