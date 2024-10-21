const estadia_alert = (title, text, icon) => {
    Swal.fire({
        title: title,
        icon: icon,
        text: text,
        showConfirmButton: false,
        timer: 2100
    })
}

const register_deleteSwal = (title, coloca, text, icon, rute) => {
    Swal.fire({
        "title": title + ' - ' + coloca,
        "text": text,
        "icon": icon,
        "showCancelButton": true,
        //"allowOutsideClick": false,
        "cancelButtonText": "Cancelar",
        "confirmButtonText": "Eliminar",
        "reverseButtons": true,
        "confirmButtonColor": "#dc3545",
    })
        .then(function (result) {
            if (result.isConfirmed) {
                // Envía la colocación del registro a eliminar
                location.href = rute + coloca
            }
        })
}

const action_alert = (text) => {
    Swal.fire({
        title: '¡Acción no permitida!',
        icon: 'warning',
        text: text,
        showConfirmButton: false,
        timer: 2100
    })
}