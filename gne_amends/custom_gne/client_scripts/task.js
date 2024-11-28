frappe.ui.form.on('Task', {
    onload: function (frm) {
        frappe.call({
            method: 'gne_amends.custom_gne.check_task_access.check_task_access',
            args: {
                task_id: frm.doc.name
            },
            callback: function (response) {
                if (!response.message) {
                    frappe.msgprint(__('You are not authorized to view this document.'));
                    frappe.set_route('List', 'Task'); // Redirect to the list view
                }
            },
            error: function (error) {
                frappe.msgprint(__('An error occurred: ') + error.message);
            }
        });
    }
});
