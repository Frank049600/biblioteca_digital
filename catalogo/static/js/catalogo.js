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
    let entrega = data['entrega'].trim().toLowerCase();
    let text = entrega == "no/entregado" ? "¿Marcar como entregado?" : "¿Marcar como NO entregado?";
    let btn = entrega == "no/entregado" ? "Marcar/entregado" : "Marcar/No entregado";
    let btn_color = entrega == "no/entregado" ? "#28a745" : "#DC4C64"; // verde(success) - rojo(danger)
    let icon = "warning";
    let rute = '/book_delivered/';
    // Llama el SweetAlert del script notification
    register_entrega(cve_prestamo, text, btn, btn_color, icon, rute, entrega);
});

// Función para renovar el prestamo del libro
$('#prestamoTable').on('click', 'tbody td a#renew_again', function (e) {
    let data = $(this).closest('#info_book').data();
    let cve_prestamo = data['cve_prestamo'];
    let cantidad = data['cantidad'];
    let entrega = data['entrega'].trim().toLowerCase();
    let text = "¿Renovar prestamos?";
    let btn = "Renovar";
    let btn_color = "#28a745";
    let icon = "warning";
    let rute = '/renew_again/';
    // Llama el SweetAlert del script notification
    register_entrega(cve_prestamo, text, btn, btn_color, icon, rute, entrega, cantidad);
});

// Valida que todos los campos esten llenos antes de mandar el formulario
$('#btnSendEstadias').on('click', function (event) {
    let matricula = $('input[name=matricula]').val(),
        nom_alumno = $('input[name=nom_alumno]').val(),
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