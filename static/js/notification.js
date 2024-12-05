const estadia_alert = (title, text, icon) => {
    Swal.fire({
        title: title,
        icon: icon,
        text: text,
        showConfirmButton: false,
        timer: 3000
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

const renew_again = (rute, cve_prestamo, cantidad) => {
    // Generar las opciones dinámicamente según la cantidad de libros
    const inputOptions = {};
    for (let i = 1; i <= cantidad; i++) {
        inputOptions[i] = i; // Por ejemplo, "Libro 1", "Libro 2", etc.
    }

    // Mostrar el SweetAlert con las opciones dinámicas
    Swal.fire({
        title: "Cantidad de libros para renovar",
        input: "select",
        inputOptions: inputOptions,
        showCancelButton: true,
        confirmButtonText: "Renovar",
        confirmButtonColor: "#28a745",
        inputValidator: (value) => {
            return new Promise((resolve) => {
                if (value) {
                    resolve();
                } else {
                    resolve("Debe seleccionar un libro.");
                }
            });
        }
    }).then((result) => {
        if (result.isConfirmed) {
            // Swal.fire(`Usted seleccionó: ${inputOptions[result.value]}`);
            location.href = rute + cve_prestamo + result.value
        }
    });
};

const register_entrega = (cve_prestamo, text, btn, btn_color, icon, rute, entrega, cantidad = false) => {
    Swal.fire({
        "title": cve_prestamo,
        "text": text,
        "icon": icon,
        "showCancelButton": true,
        //"allowOutsideClick": false,
        "cancelButtonText": "Cancelar",
        "confirmButtonText": btn,
        "reverseButtons": true,
        "confirmButtonColor": btn_color,
    })
        .then(function (result) {
            if (result.isConfirmed) {
                // Envía la colocación del registro a eliminar
                if (cantidad) {
                    renew_again(rute, cve_prestamo, cantidad)
                }
                else {
                    location.href = rute + cve_prestamo
                }
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
