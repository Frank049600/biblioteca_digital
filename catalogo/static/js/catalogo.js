// Llama función para DataTable
datatable('catalogoTable');
datatable('prestamoTable');

//Buscar matricula
$('#modal_catalogo').on('shown.bs.modal', function () {
    //let matricula = $('#id_matricula').val()
    let matricula = $('#catalogoTable tbody tr').data('persona')
    if (matricula != '') {
        $('#msg_search').attr('style', 'display:block')
        $.ajax({
            url: '/get_personas_p/',
            data: { "matricula": matricula },
            type: 'GET',
            success: function (response) {
                let nombre_completo = response['nombre'] + ' ' + response['apellido_paterno'] + ' ' + response['apellido_materno'];
                let carrera = response['nombre_grupo'];
                $('input[name=matricula').val(matricula);
                $('input[name=nom_alumno]').val(nombre_completo);
                $('input[name=carrera_grupo]').val(carrera);
            },
            error: function (error) {
                $('input[name=matricula]').val('');
                $('input[name=nom_alumno]').val('');
                $('input[name=carrera_grupo]').val('');
            }
        });
    }
});

$('#catalogoTable').on('click', 'tbody tr td a#btnPedidoBook', function () {
    let data = $(this).closest('tr').data()
    let portada = 'data:image/png;base64,';
    // Convierte la imagen
    portada_base64 = data.base64 != 'None' ? portada + data.base64 : portada + default_img()
    
    $('#content_portada').attr("src",portada_base64);
    $('input[name=nom_libro]').val(data.titulo);
    $('input[name=nom_autor]').val(data.autor);
    $('input[name=edicion]').val(data.edicion);
    $('input[name=colocacion]').val(data.colocacion);
});

// Función para el borrado de elementos
$('#prestamoTable').on('click', 'tbody td a#delivered', function (e) {
    let data = $(this).closest('#info_book').data();
    let cve_prestamo = data['cve_prestamo'];
    // let entrega = data['entrega'].trim().toLowerCase();
    let entrega = data['entrega']
    let text = entrega == "Proceso" ? "¿Marcar como entregado?" : "¿Marcar como devuelto?";
    let btn = entrega == "Proceso" ? "Marcar/entregado" : "Marcar/devuelto";
    let btn_color = entrega == "Proceso" ? "#28a745" : "#18632a";
    let icon = "question";
    let rute = '/book_delivered/';
    if (entrega == 'Devuelto') {
        process_repeat();
    }
    else {
        // Llama el SweetAlert del script notification
        register_entrega(cve_prestamo, text, btn, btn_color, icon, rute, entrega);
    }
});

// Función para renovar el prestamo del libro
$('#prestamoTable').on('click', 'tbody td a#renew_again', function (e) {
    let data = $(this).closest('#info_book').data();
    let cve_prestamo = data['cve_prestamo'];
    let cantidad_m = data['cantidad_m'];
    let cantidad_i = data['cantidad_i'];
    // let entrega = data['entrega'].trim().toLowerCase();
    let entrega = data['entrega'];
    let title = "¿Renovar prestamo?";
    let btn = "Renovar";
    // Validar si es posible eliminar
    let btn_color = "#28a745"; // Botón renovar
    let icon = "question";
    let rute = '/renew_again/';
    // Llama el SweetAlert del script notification
    register_renew(cve_prestamo, title, btn, btn_color, icon, cantidad_i , cantidad_m, rute, entrega);
});

// Valida que todos los campos esten llenos antes de mandar el formulario
$('#btnSendEstadias').on('click', function (event) {
    let matricula = $('input[name=matricula]').val(),
        nom_alumno = $('input[name=nom_alumno]').val(),
        colocacion = $('input[name=colocacion]').val(),
        cantidad = $('input[name=cantidad_i]').val(),
        carrera_grupo = $('input[name=carrera_grupo]').val();

    if(matricula == '' && nom_alumno == '' && carrera_grupo == ''){
        event.preventDefault();
    }

})

$('#modal_catalogo').on('hidden.bs.modal', function () {
    $('#msg_search').attr('style', 'display:none');
    $('#msg_error').attr('style', 'display:none');
    $('#msg_success').attr('style', 'display:none');
    $('input[name=nom_libro]').val('');
    $('input[name=nom_autor]').val('');
    $('input[name=edicion]').val('');
    $('input[name=colocacion]').val('');
    $('input[name=cantidad]').val('');
    $('input[name=matricula]').val('');
    $('input[name=nom_alumno]').val('');
    $('input[name=carrera_grupo]').val('');
    $('#content_portada').attr("src","#");
});

// Función para realizar salto de input con Enter
tabIndex_form('modal_catalogo', true);