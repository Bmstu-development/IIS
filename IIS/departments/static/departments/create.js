$(function () {
    // $(".form-check-input").prop('checked', false);
})

function saveClick() {
    let name_input = $('#id_name')[0];
    if (!name_input.value) {
        name_input.classList.add('is-invalid');
        $(".is-invalid:first").get(0).scrollIntoView();
        return;
    } else {
        name_input.classList.remove('is-invalid');
    }
    let descr_input = $('#id_descr')[0];
    if (!descr_input.value) {
        descr_input.classList.add('is-invalid');
        $(".is-invalid:first").get(0).scrollIntoView();
        return;
    } else {
        descr_input.classList.remove('is-invalid');
    }
    $('#id-save-modal').modal('show');
}
