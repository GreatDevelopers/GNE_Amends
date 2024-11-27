import frappe

def get_task_permission_query_conditions(user):
    if not user:
        user = frappe.session.user

    # Check if the user has the "Task Completer" role
    if "Task Completer" in frappe.get_roles(user):
        # Restrict to tasks assigned to the user
        return f"""`tabTask`.name IN (
            SELECT `reference_name`
            FROM `tabToDo`
            WHERE `tabToDo`.reference_type = 'Task' AND `tabToDo`.allocated_to = '{user}'
        )"""
    else:
        # Return an empty condition for other users to follow role-based permissions
        return ""
