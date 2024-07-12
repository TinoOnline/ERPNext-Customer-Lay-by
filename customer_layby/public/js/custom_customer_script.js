frappe.ui.form.on('Customer', {
    // the mulitple triggers allows the check to be carried out in realtime as fields are being edited
    refresh(frm) {
        check_lay_by_eligibility(frm)
    },
    custom_id_number(frm){
        check_lay_by_eligibility(frm)
    },
    custom_passport_number(frm){
        check_lay_by_eligibility(frm)
    },
    custom_passport_country(frm){
        check_lay_by_eligibility(frm)
    },
    custom_verification_type(frm){
        check_lay_by_eligibility(frm)
    }
});

function check_lay_by_eligibility(frm) {
    frm.set_value('custom_layby_eligible', false);
    // 9 indicates the smallest the phone number can be, as it can be greater with the use of the country code (27)
    if (frm.doc.custom_verification_type === 'ID') {
        if (frm.doc.custom_id_number && frm.doc.custom_id_number.length === 13 && frm.doc.mobile_no && frm.doc.mobile_no.length > 9) {
            frm.set_value('custom_layby_eligible', true);
        }
    } else if (frm.doc.custom_verification_type === 'Passport') {
        if (frm.doc.custom_passport_number && frm.doc.custom_passport_country && frm.doc.mobile_no && frm.doc.mobile_no.length > 9) {
            frm.set_value('custom_layby_eligible', true);
        }
    }
}