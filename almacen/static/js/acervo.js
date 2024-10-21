$(document).ready(function () {
    new DataTable('#acervoTable', {
        //columnDefs: [
        //    { orderable: false, target: [9] }
        //],
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

    // Se estructura la información para el modal
    function struct_modal(title, autor, editorial, cantidad, colocacion, edicion, año, type_adqui, state, formato) {
        let match = {
            'EXC': 'Excelente',
            'BUE': 'Bueno',
            'REG': 'Regular',
            'MAL': 'Malo'
        };
        for (let i = 0; i < 4; i++) {
            if (match[state.toString()] != undefined) {
                state = match[state.toString()]
            };
        };
        formato = formato == 'book' ? 'Libro' : (formato == 'disc' ? 'Disco' : '');
        let struct = '<div class="info-box mb-3" style="background-color: #3c6382; color: white;">'
            + '<span class="info-box-icon"><i class="fas fa-heading"></i></span>'
            + '<div class="info-box-content">'
            + '<span class="info-box-text">Título</span>'
            + '<span class="info-box-number">' + title + '</span>'
            + '</div>'
            + '</div>'
            + '<div class="row">'
            + '<div class="col-xl-6">'
            + '<div class="info-box mb-3" style="background-color: #0a3d62; color: white;">'
            + '<span class="info-box-icon"><i class="fas fa-feather-alt"></i></span>'
            + '<div class="info-box-content">'
            + '<span class="info-box-text">Autor</span>'
            + '<span class="info-box-number">' + autor + '</span>'
            + '</div>'
            + '</div>'
            + '</div>'
            + '<div class="col-xl-6">'
            + '<div class="info-box mb-3" style="background-color: #002078; color: white;">'
            + '<span class="info-box-icon"><i class="fas fa-user-edit"></i></span>'
            + '<div class="info-box-content">'
            + '<span class="info-box-text">Editorial</span>'
            + '<span class="info-box-number">' + editorial + '</span>'
            + '</div>'
            + '</div>'
            + '</div>'
            + '</div>'
            + '<div class="row">'
            + '<div class="col-xl-6">'
            + '<div class="info-box mb-3" style="background-color: #0a3d62; color: white;">'
            + '<span class="info-box-icon"><i class="fas fa-boxes"></i></span>'
            + '<div class="info-box-content">'
            + '<span class="info-box-text">Cantidad</span>'
            + '<span class="info-box-number">' + cantidad + '</span>'
            + '</div>'
            + '</div>'
            + '</div>'
            + '<div class="col-xl-6">'
            + '<div class="info-box mb-3" style="background-color: #002078; color: white;">'
            + '<span class="info-box-icon"><i class="fas fa-wave-square"></i></span>'
            + '<div class="info-box-content">'
            + '<span class="info-box-text">Colocación</span>'
            + '<span class="info-box-number">' + colocacion + '</span>'
            + '</div>'
            + '</div>'
            + '</div>'
            + '</div>'
            + '<div class="row">'
            + '<div class="col-xl-6">'
            + '<div class="info-box mb-3" style="background-color: #0a3d62; color: white;">'
            + '<span class="info-box-icon"><i class="fas fa-newspaper"></i></span>'
            + '<div class="info-box-content">'
            + '<span class="info-box-text">Edición</span>'
            + '<span class="info-box-number">' + edicion + '</span>'
            + '</div>'
            + '</div>'
            + '</div>'
            + '<div class="col-xl-6">'
            + '<div class="info-box mb-3" style="background-color: #002078; color: white;">'
            + '<span class="info-box-icon"><i class="fas fa-calendar-alt"></i></span>'
            + '<div class="info-box-content">'
            + '<span class="info-box-text">Año de publicación</span>'
            + '<span class="info-box-number">' + año + '</span>'
            + '</div>'
            + '</div>'
            + '</div>'
            + '</div>'
            + '<div class="row">'
            + '<div class="col-xl-6">'
            + '<div class="info-box mb-3" style="background-color: #0a3d62; color: white;">'
            + '<span class="info-box-icon"><i class="fas fa-shopping-cart"></i></span>'
            + '<div class="info-box-content">'
            + '<span class="info-box-text">Tipo de adquisición</span>'
            + '<span class="info-box-number">' + type_adqui + '</span>'
            + '</div>'
            + '</div>'
            + '</div>'
            + '<div class="col-xl-3">'
            + '<div class="info-box mb-3" style="background-color: #002078; color: white;">'
            + '<span class="info-box-icon"><i class="fas fa-eye"></i></span>'
            + '<div class="info-box-content">'
            + '<span class="info-box-text">Estado</span>'
            + '<span class="info-box-number">' + state + '</span>'
            + '</div>'
            + '</div>'
            + '</div>'
            + '<div class="col-xl-3">'
            + '<div class="info-box mb-3" style="background-color: #002078; color: white;">'
            + '<span class="info-box-icon"><i class="fas fa-book fa-xs"></i>/<i class="fas fa-compact-disc fa-xs"></i></span>'
            + '<div class="info-box-content">'
            + '<span class="info-box-text">Formato</span>'
            + '<span class="info-box-number">' + formato + '</span>'
            + '</div>'
            + '</div>'
            + '</div>'
            + '</div>'
        return struct
    }

    // Función para mostrar todo el registro en un modal
    $('#acervoTable').on('click', 'tbody tr td a#more_info', function () {
        // Se obtienen todos los datos de la tabla
        let data = $(this).closest('tr').data(),
            title = data['title'],
            autor = data['autor'],
            editorial = data['edit'],
            cantidad = data['cant'],
            colocacion = data['coloca'],
            edicion = data['edicion'],
            año = data['anio'],
            type_adqui = data['adqui'],
            state = data['state'],
            formato = data['formato']

        // Se agrega todo el elemento html iterando la información obtenida
        $('#show_more').append(struct_modal(title, autor, editorial, cantidad, colocacion, edicion, año, type_adqui, state, formato));

        // Se abre el modal una vez cargada la información
        $('#more_info_modal').modal('show')
        // Se detecta el cerrado del modal
        $('#more_info_modal').on('hidden.bs.modal', function () {
            // Se realiza el borrado de los elementos hijo de la etiqueta indicada
            $('#show_more').children().remove()
        })
    })

    // Función para el borrado de elementos
    $('#acervoTable').on('click', 'tbody #info_data td a#remove_register', function (e) {
        let data = $(this).closest('#info_data').data(),
            coloca = data['coloca'],
            title = data['title'],
            text = "El registro no se podrá recuperar",
            icon = "warning",
            rute = '/delete_acervo/'
        // Llama el SweetAlert del script notification
        register_deleteSwal(title, coloca, text, icon, rute)
    })

    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    // Función para edición
    $('#acervoTable').on('click', 'tbody #info_data td a#edit_register', function () {
        // Se obtiene la información de la tabla
        let moreInfo = $(this).closest('#info_data').data();
        // Se identifica el ID del modal
        let modal_inputs = $('#acervo_add')
        // Arreglo de nombre de los campos
        let input_id = ['titulo', 'autor', 'editorial', 'anio', 'edicion', 'cant', 'colocacion', 'formato', 'adqui', 'estado']
        // codificación para los valores en los inputs SELECT
        decode_val = {
            'Libro': 'book',
            'Disco': 'disc',
            'book': 'book',
            'disc': 'disc',
            'Excelente': 'EXC',
            'Bueno': 'BUE',
            'Regular': 'REG',
            'Malo': 'MAL',
            'EXC': 'EXC',
            'BUE': 'BUE',
            'REG': 'REG',
            'MAL': 'MAL'
        }
        // Se asigna el valor a los input
        // $('#tbl_addBook #' + input_id[0])[0].value = moreInfo['title'] // Campo titulo
        $('input[name="' + input_id[0] + '"]').val(moreInfo['title'])
        $('input[name="' + input_id[1] + '"]').val(moreInfo['autor']) // Campo Autor
        $('input[name="' + input_id[2] + '"]').val(moreInfo['edit']) // Campo editorial
        $('input[name="' + input_id[3] + '"]').val(moreInfo['anio']) // Campo año
        $('input[name="' + input_id[4] + '"]').val(moreInfo['edicion']) // Campo edición
        $('input[name="' + input_id[5] + '"]').val(moreInfo['cant']) // Campo cantidad
        $('input[name="' + input_id[6] + '"]').val(moreInfo['coloca']) // Campo colocación
        $('select[name="' + input_id[7] + '"]').val(decode_val[moreInfo['formato']]) // campo formato
        $('input[name="' + input_id[8] + '"]').val(moreInfo['adqui']) //Campo tipo de adquisición
        $('select[name="' + input_id[9] + '"]').val(decode_val[moreInfo['state']]) // Campo estado
        $('#acervo_add #tbl_addBook').attr('action', '/edit_acervo/')
        // Se abre el modal al final de la asignación de valores en los inputs
        modal_inputs.modal('show')
        $('#acervo_add #btnModalSend').attr('style', 'display: none')
        $('#acervo_add #btnModalUpdate').removeAttr('style', 'display: none;')
        // Al cerrar el modal se limpian todos los campos.
        modal_inputs.on('hidden.bs.modal', function () {
            for (let i = 0; i < 10; i++) {
                if (i != 7 && i != 9) {
                    // $('#tbl_addBook #' + input_id[i])[0].value = ''
                    $('input[name="' + input_id[i] + '"]').val('')
                }
                //$('#tbl_addBook #' + input_id[7])[0].value = 'book'
                $('select[name="' + input_id[7] + '"]').val('book')
                //$('#tbl_addBook #' + input_id[9])[0].value = 'EXC'
                $('select[name="' + input_id[9] + '"]').val('EXC')
                $('#acervo_add #btnModalUpdate').attr('style', 'display: none;')
                $('#acervo_add #btnModalSend').removeAttr('style', 'display: none;')
                $('#acervo_add #tbl_addBook').attr('action', '/acervo_registro/')
            }
        })
    })
})

