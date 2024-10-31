$(function () {

    new DataTable('#ProyectosTable', {
        layout: {
            bottomEnd: {
                paging: {
                    boundaryNumbers: false
                }
            }
        },
        language:
        {
            "aria": {
                "sortAscending": "Activar para ordenar la columna de manera ascendente",
                "sortDescending": "Activar para ordenar la columna de manera descendente"
            },
            "infoThousands": ",",
            "loadingRecords": "Cargando...",
            "paginate": {
                "first": "Primero",
                "last": "Último",
                "next": "Siguiente",
                "previous": "Anterior"
            },
            "processing": "Procesando...",
            "search": "Buscar:",
            "searchPanes": {
                "clearMessage": "Borrar todo",
                "count": "{total}",
                "showMessage": "Mostrar Todo"
            },
            "thousands": ",",
            "datetime": {
                "previous": "Anterior",
                "hours": "Horas",
                "minutes": "Minutos",
                "seconds": "Segundos",
                "unknown": "-",
                "amPm": [
                    "am",
                    "pm"
                ],
                "next": "Siguiente",
                "months": {
                    "0": "Enero",
                    "1": "Febrero",
                    "10": "Noviembre",
                    "11": "Diciembre",
                    "2": "Marzo",
                    "3": "Abril",
                    "4": "Mayo",
                    "5": "Junio",
                    "6": "Julio",
                    "7": "Agosto",
                    "8": "Septiembre",
                    "9": "Octubre"
                },
                "weekdays": [
                    "Domingo",
                    "Lunes",
                    "Martes",
                    "Miércoles",
                    "Jueves",
                    "Viernes",
                    "Sábado"
                ]
            },
            "decimal": ".",
            "emptyTable": "No hay datos disponibles en la tabla",
            "zeroRecords": "No se encontraron coincidencias",
            "info": "Mostrando _START_ a _END_ de _TOTAL_ entradas",
            "infoFiltered": "(Filtrado de _MAX_ total de entradas)",
            "lengthMenu": "Mostrar _MENU_ entradas",
            "stateRestore": {
                "creationModal": {
                    "search": "Buscar",
                    "button": "Crear"
                },
            },
            "infoEmpty": "No hay datos para mostrar"
        }
    })
})

let response
response = $('#response_sweetalert').data('resp')

let title, text, icon
if (response == 'success') {
    title = 'Correcto'
    text = 'Registro exitoso'
    icon = 'success'
    estadia_alert(title, text, icon)
}

if (response == 'error') {
    title = 'Error'
    text = '¡Algo salio mal!'
    icon = 'error'
    estadia_alert(title, text, icon)
}

let iframe = $('#proyectos_preview')
if (iframe.length != 0) {
    // Función que evita el copiado de texto en la página del preview
    function notCopy() {
        action_alert('La acción de copiado no esta permitida');
    }
    // Función que evita la el click derecho dentro de la página del preview
    notClicRight = document.getElementById('iframe_card');
    page = document.getElementById('proyectos_preview');
    notClicRight.addEventListener('contextmenu', function (e) {
        e.preventDefault();
    });
    // Función para evitar la impresión de pantalla
    document.addEventListener('keydown', (event) => {
        if (event.ctrlKey) {
            if (event.keyCode == 80) {
                action_alert('La acción de impresión no esta permitida')
                event.preventDefault();
            }
        }
    });
    // Función para el pintado del reporte en modo canvas dentro de la página
    let url = $('#pdfViewer').data('url_reporte');
    var loadingTask = pdfjsLib.getDocument({ url: url });
    loadingTask.promise.then(function (pdf) {
        // Se obtiene el número total de páginas del PDF
        let total_pages = pdf.numPages;

        for (let i = 1; i <= total_pages; i++) {
            (function (pageNumber) {

                pdf.getPage(pageNumber).then(function (page) {
                    var scale = 0.8;
                    var viewport = page.getViewport({ scale: scale });

                    var canvas = document.createElement('canvas');
                    var context = canvas.getContext('2d');
                    canvas.height = viewport.height;
                    canvas.width = viewport.width;

                    var renderContext = {
                        canvasContext: context,
                        viewport: viewport
                    };
                    page.render(renderContext).promise.then(function () {
                        console.log('Página renderizada');
                    });

                    document.getElementById('pdfViewer').appendChild(canvas);
                }).catch(function (error) {
                    console.log('Error al cargar la página ' + pageNumber + ' del PDF: ', error);
                });
            })(i);
        }
    }).catch(function (error) {
        console.log('Error al cargar el PDF: ', error);
    });
}

$('#modal_registro').on('shown.bs.modal', function () {
    let asesor = $('#data_academico').data('academico');
    $('input[name=asesor_academico]').val(asesor);

    $('#btn_search_matricula').on('click', function (e) {
        let matricula = $('#id_matricula').val()
        if (matricula != '') {
            $('#msg_search').attr('style', 'display:block')
            $.ajax({
                url: '/get_alumno/',
                data: { "matricula": matricula },
                type: 'GET',
                success: function (response) {
                    $('#msg_search').attr('style', 'display:none');
                    $('#msg_error').attr('style', 'display:none');
                    $('#msg_success').attr('style', 'display:block');
                    let nombre_completo = response['nombre'] + ' ' + response['apellido_paterno'] + ' ' + response['apellido_materno'];
                    let carrera = response['nombre_grupo'];
                    $('input[name=alumno]').val(nombre_completo);
                    $('input[name=carrera]').val(carrera);
                },
                error: function (error) {
                    $('#msg_success').attr('style', 'display:none');
                    $('#msg_search').attr('style', 'display:none');
                    $('#msg_error').attr('style', 'display:block');
                    $('input[name=alumno]').val('');
                    $('input[name=carrera]').val('');
                }
            })
        }
    })
})

$('#modal_registro').on('hidden.bs.modal', function () {
    $('#msg_search').attr('style', 'display:none');
    $('#msg_error').attr('style', 'display:none');
    $('#msg_success').attr('style', 'display:none');
    $('input[name=proyecto]').val('');
    $('input[name=matricula]').val('');
    $('input[name=alumno]').val('');
    $('input[name=carrera]').val('');
    $('input[name=generacion]').val('');
    $('input[name=empresa]').val('');
    $('input[name=asesor_orga]').val('');
    $('input[name=reporte]').val('');
})
