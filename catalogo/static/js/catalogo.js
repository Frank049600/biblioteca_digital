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
            url: '/get_alumno/',
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
});

$('#catalogoTable').on('click', 'tbody tr td a#btnPedidoBook', function () {
    let data = $(this).closest('tr').data()
//    console.log(data)
    $('input[name=nom_libro]').val(data.titulo);
    $('input[name=nom_autor]').val(data.autor);
    $('input[name=edicion]').val(data.edicion);
    $('input[name=colocacion]').val(data.colocacion);
});

// Función para realizar salto de input con Enter
tabIndex_form('modal_catalogo', true);