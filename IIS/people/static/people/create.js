$(function () {
    let patronymic_input = $('#id_patronymic');
    let phone_number_input = $('#id_phone_number');
    let tg_username_input = $('#id_tg_username');
    let patronymic_checkbox = $('#id_no_patronymic');
    let phone_number_checkbox = $('#id_no_phone_number');
    let tg_username_checkbox = $('#id_no_tg_username');

    if (patronymic_checkbox.is(':checked')) {
        patronymic_input.parent().hide();
        patronymic_input[0].value = '';
    }

    if (phone_number_checkbox.is(':checked')) {
        phone_number_input.parent().hide();
        phone_number_input[0].value = '';
    }

    if (tg_username_checkbox.is(':checked')) {
        tg_username_input.parent().hide();
        tg_username_input[0].value = '';
    }

    patronymic_checkbox.change(function () {
        if (this.checked) {
            patronymic_input.parent().hide();
            patronymic_input[0].value = '';
        } else {
            patronymic_input.parent().show();
        }
    })

    phone_number_checkbox.change(function () {
        if (this.checked) {
            phone_number_input.parent().hide();
            phone_number_input[0].value = '';
        } else {
            phone_number_input.parent().show();
        }
    })

    tg_username_checkbox.change(function () {
        if (this.checked) {
            tg_username_input.parent().hide();
            tg_username_input[0].value = '';
        } else {
            tg_username_input.parent().show();
        }
    })
})

function validatePhoneNumber(ph_num) {
    let re = new RegExp('^\\+7(\\s\\(\\d{3}\\))(\\s\\d{3})(?:-\\d{2}){2}$');
    return re.test(ph_num);
}

function validateTgUsername(tg_uname) {
    let re = new RegExp('^@(\\w{4,})$');
    return re.test(tg_uname);
}

function savePersonClick() {
    let is_invalid_fields = false;

    let surname_input = $('#id_surname')[0];
    if (!surname_input.value) {
        surname_input.classList.add('is-invalid');
        $(".is-invalid:first").get(0).scrollIntoView();
        is_invalid_fields = true;
    } else {
        surname_input.classList.remove('is-invalid');
    }

    let name_input = $('#id_name')[0];
    if (!name_input.value) {
        name_input.classList.add('is-invalid');
        $(".is-invalid:first").get(0).scrollIntoView();
        is_invalid_fields = true;
    } else {
        name_input.classList.remove('is-invalid');
    }

    let patronymic_input = $('#id_patronymic')[0];
    if (!patronymic_input.value && !$('#id_no_patronymic').is(":checked")) {
        patronymic_input.classList.add('is-invalid');
        $(".is-invalid:first").get(0).scrollIntoView();
        is_invalid_fields = true;
    } else {
        patronymic_input.classList.remove('is-invalid');
    }

    let organisation_input = $('#id_organisation')[0];
    if (!organisation_input.value) {
        organisation_input.classList.add('is-invalid');
        $(".is-invalid:first").get(0).scrollIntoView();
        is_invalid_fields = true;
    } else {
        organisation_input.classList.remove('is-invalid');
    }

    let phone_input = $('#id_phone_number')[0];
    if (!$('#id_no_phone_number').is(":checked") && (!phone_input.value ||
        !validatePhoneNumber(phone_input.value))) {
        phone_input.classList.add('is-invalid');
        $(".is-invalid:first").get(0).scrollIntoView();
        is_invalid_fields = true;
    } else {
        phone_input.classList.remove('is-invalid');
    }

    let tg_username_input = $('#id_tg_username')[0];
    if (!$('#id_no_tg_username').is(":checked") && (!phone_input.value ||
        !validateTgUsername(tg_username_input.value))) {
        tg_username_input.classList.add('is-invalid');
        $(".is-invalid:first").get(0).scrollIntoView();
        is_invalid_fields = true;
    } else {
        tg_username_input.classList.remove('is-invalid');
    }

    if (!is_invalid_fields) {
        if ($('#id_is_user').is(':checked')) {
            $('#id-create-user-modal').modal('show');
            return
        }
        alert('OK!');
    }
}

function createUser() {
    $('#id-create-user-modal').modal('hide');
    $('#id-logpass-modal').modal('show');
}
