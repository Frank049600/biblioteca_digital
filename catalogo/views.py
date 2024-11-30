from django.shortcuts import render, redirect
from almacen.models import acervo_model
from catalogo.models import model_catalogo
from django.contrib import messages
from .forms import catalogo_form
from django.utils.timezone import now
import json
import base64
from django.http import JsonResponse
from django.utils.timezone import now

from static.helpers import *

# Create your views here.
def catalago_View(request):
    form = catalogo_form()
    side_code = 400
    listado = acervo_model.objects.all()
    return render(request, 'index_catalogo.html', {"side_code": side_code, "listado":listado, "form":form})

@login_required
@groups_required('Administrador')
def prestamos_View(request):
    side_code = 401
    listado = model_catalogo.objects.all()

    dias_permitidos = 6
    data = {}
    data_all = []
    cont = 0

    for f in listado:
        data = {
            "nom_alumno": f.nom_alumno,
            "matricula": f.matricula,
            "carrera_grupo": f.carrera_grupo,
            "nom_libro": f.nom_libro,
            "nom_autor": f.nom_autor,
            "colocacion": f.colocacion,
            "cantidad": f.cantidad,
            "tipoP": f.tipoP,
        }   

        if f.tipoP == 'Externo':
            fecha_limite = f.fechaP
            # Fecha actual en la zona horaria configurada
            ahora = now().replace(microsecond=0)
            # Calculamos la diferencia entre las fechas
            diferencia = ahora - fecha_limite
            # Obtener el número de días de la diferencia
            dias_transcurridos = diferencia.days

            dias_restantes = dias_permitidos - dias_transcurridos

            data["dias_restantes"] = dias_restantes
            
        data_all.append(data)

    return render(request, 'index_prestamos.html', {"side_code": side_code, "data_all": data_all})

def get_alumno(request):
    matricula = request.GET.get('matricula')
    if matricula:
        cve_persona = ''
        try:
            # alumno_grupo = get_object_or_404(AlumnoGrupo, matricula=matricula)
            alumno_grupo = AlumnoGrupo.objects.filter(matricula=matricula).values_list('cve_grupo', flat=True)
            cve_grupo = alumno_grupo[len(alumno_grupo) - 1]
            grupo = Grupo.objects.get(cve_grupo=cve_grupo)
            carrera = Carrera.objects.get(nombre=grupo.cve_carrera)
            generacion = Alumno.objects.get(matricula=matricula)
            cve_persona = Usuario.objects.get(login=matricula)
            persona = Persona.objects.get(cve_persona=cve_persona.cve_persona)
            data = {
                "nombre": persona.nombre,
                "apellido_paterno": persona.apellido_paterno,
                "apellido_materno": persona.apellido_materno,
                "nombre_grupo": grupo.nombre,
                "nombre_carrera": carrera.nombre,
                "generacion": generacion.generacion
            }
            # print(data['nombre'])
            return JsonResponse(data)
        except Exception as a:
            print(f"Algo salio mal: {a}")
    return JsonResponse({'error': 'Matricula no proporcionada'}, status=400)


def prestamo_registro(request):
    if request.method == 'POST':
        form = catalogo_form(request.POST)
        print(form)
        if form.is_valid():
            nom_libro = form.cleaned_data['nom_libro']
            nom_autor = form.cleaned_data['nom_autor']
            edicion = form.cleaned_data['edicion']
            colocacion = form.cleaned_data['colocacion']
            cantidad = form.cleaned_data['cantidad']
            matricula = form.cleaned_data['matricula']
            nom_alumno = form.cleaned_data['nom_alumno']
            carrera_grupo = form.cleaned_data['carrera_grupo']
            tipoP = form.cleaned_data['tipoP']
            fechaP = now().replace(microsecond=0)

            catalago_View=model_catalogo.objects.create(
                    nom_libro = nom_libro,
                    nom_autor = nom_autor,
                    edicion = edicion,
                    colocacion = colocacion,
                    cantidad = cantidad,
                    matricula = matricula,
                    nom_alumno = nom_alumno,
                    carrera_grupo = carrera_grupo,
                    tipoP = tipoP,
                    fechaP = fechaP
            )
            messages.add_message(request, messages.SUCCESS, 'Prestamo Solicitado')
            # Redirigir a la vista deseada
            return redirect('catalago_View')
        else:
            # Si el formulario no es válido, vuelve a renderizar el formulario con errores
            messages.add_message(request, messages.ERROR, '¡Por favor, corrija los errores del formulario!')
            return redirect('catalago_View')
    else:
        # Si no es un POST, se asume que es un GET
        form = catalogo_form()
        messages.add_message(request, messages.ERROR, '¡Algo salio mal!')
        return redirect('catalago_View')

# Función para convertir documento a base64
def convert_base64(doc):
    # Se convierte el pdf en formato base64
    # Lee el documento que llega en formulario
    file = doc.read()
    # Convierte el documento en base64
    encoded_string = base64.b64encode(file)
    return encoded_string.decode('utf-8')

def temporary_image_base64(base_64_input):
    # base64_string = base_64_input.strip().split(',')[1]
    decoded_bytes = base64.b64decode(base_64_input)
    file_temp, path_temp = tempfile.mkstemp(suffix=".webp", dir=settings.MEDIA_ROOT + "/")
    try:
        with os.fdopen(file_temp, 'wb') as tmp:
            tmp.write(decoded_bytes)
    except Exception as e:
        os.remove(path_temp)
        raise e
    return path_temp

@login_required
@groups_required('Alumno', 'Docente')
def view_book(request, report_rute):
    try:
        id_reporte = model_estadias.objects.filter(reporte=report_rute).first()
        # Se crea el archivo temporal y se obtiene la ruta
        name_temp = temporary_file_base_64(id_reporte.base64)
        # Se separan los datos no necesarios
        ruta = name_temp.split('/code')[1]

# Caga la vista con la información del acervo
def cargar_portada(request):
    form = catalogo_form()
    return render(request, 'cargar_portada.html', {"form":form})

# Función que realiza la edición del elemento con la imagen de portada
def edit_portada(request):
    if request.method == 'POST':
        data = {}
        cont = 1
        colocacion = ''
        # Se almacena la imagen entrante con el nombre del libro que le corresponde.
        for r in request.FILES:
            data[cont] = [r, request.POST.get(f"titulo-{cont}")]
            cont += 1

        # Se realiza el guardado de la imagen con el libro indicado
        for d in range(len(data)):
            # print(data[d+1][1]) # Se obtiene el nombre del libro

            # return redirect('cargar_portada')
            colocacion = request.POST.get('colocacion')  # Obtén la colocación del formulario
            nueva_portada = request.FILES[data[d+1][0]]  # Obtén el archivo subido

            if not colocacion or not nueva_portada:
                messages.error(request, 'Falta información: colocación o archivo de portada.')
                return redirect('cargar_portada')  # Redirige con un mensaje de error

            # Buscar el registro en la base de datos por `colocacion`
            acervo_update = acervo_model.objects.filter(colocacion=colocacion, titulo=data[d+1][1]).first()

            if acervo_update:
                # Almacenar el nuevo archivo de portada}
                acervo_update.base64 = convert_base64(nueva_portada)
                acervo_update.fechaedicion = now().replace(microsecond=0)
                acervo_update.save()
                
            else:
                messages.error(request, 'No se encontró un registro con la colocación proporcionada.')
                return redirect('cargar_portada')  # Redirige con un mensaje de error
        messages.success(request, 'Portada actualizada exitosamente.')
        return redirect('cargar_portada')  # Redirige al éxito
    else:
        messages.error(request, 'Solicitud inválida.')
        return redirect('cargar_portada')


def search_book(request):
    get_colocacion = request.GET.get('colocacion')
    if get_colocacion:
        try:
            book_data = {}
            data_all = []
            # book = acervo_model.objects.get(colocacion=str(get_colocacion))
            book = acervo_model.objects.all()
            for b in book:
                if b.colocacion == get_colocacion:
                    book_data = {
                        'colocacion': b.colocacion,
                        'titulo': b.titulo,  # Replace with actual fields of your model
                        'autor': b.autor,
                        'anio': b.anio,
                        'edicion': b.edicion
                        # Add other fields as needed
                    }
                    data_all.append(book_data)
            # Return the data as a JSON response
            return JsonResponse({'status': 'success', 'books': data_all})

        except acervo_model.DoesNotExist:
            # Handle case where the book is not found
            return JsonResponse({'status': 'error', 'message': 'Book not found'}, status=404)

        except Exception as e:
            # Handle any other errors
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

    # If no 'colocacion' was provided in the GET request
    return JsonResponse({'status': 'error', 'message': 'No colocacion provided'}, status=400)
