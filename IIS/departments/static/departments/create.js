let current_req = null;

// $('#id-save').click( function(e) {
function saveDepartmentClick() {
    // e.preventDefault();

    let activists = [];
    $('table tr').each(function (row) {
        if ($(this).find('td input').is(':checked')) {
            activists.push($(this).attr('person-id'));
        }
    });
    console.log('entered')

    // current_req = $.ajax({
    //     url: window.location.href,
    //     type: 'POST',
    //     headers: {'X-CSRFToken': $('input[name="csrfmiddlewaretoken"]').attr('value')},
    //     data: {
    //         'name': $('#id_name')[0] + '1',
    //         'descr': $('#id_descr')[0],
    //         'permissions': $('#id_permissions').find(':selected').attr('value'),
    //         'supervisor': $('#id_supervisor_instance').find(':selected').attr('value'),
    //         'activists': activists,
    //     },
    //     dataType: 'json',
    //     beforeSend: function () {
    //         console.log(activists)
    //         if (current_req) {
    //             current_req.abort();
    //         }
    //     },
    //     success: function () {
    //
    //     },
    //     error: function (xhr, status, error) {
    //         console.log(error);
    //     }
    // });
}

function validateClick() {
    let invalid_fields_num = 0;

    let name_input = $('#id_name')[0];
    if (!name_input.value) {
        name_input.classList.add('is-invalid');
        $(".is-invalid:first").get(0).scrollIntoView();
        invalid_fields_num++;
    } else {
        name_input.classList.remove('is-invalid');
    }
    let descr_input = $('#id_descr')[0];
    if (!descr_input.value) {
        descr_input.classList.add('is-invalid');
        $(".is-invalid:first").get(0).scrollIntoView();
        invalid_fields_num++;
    } else {
        descr_input.classList.remove('is-invalid');
    }

    if (!invalid_fields_num) {
        $('#id-save-modal').modal('show');
    }
}
