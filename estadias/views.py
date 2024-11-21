from django.shortcuts import render, redirect
from .models import model_estadias, register_view
from .forms import estadias_form
import os
from django.http import FileResponse
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from static.helpers import *
from django.contrib import messages
from static.utils import dd
from sito.models import Alumno, AlumnoGrupo, Grupo, Carrera, Usuario, Persona, Periodo
from static.context_processors import group_permission
from django.http import JsonResponse
import base64
import tempfile
import time
from django.utils.timezone import localtime

from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404

def add_group_name_to_contex(view_class):
    original_dispatch = view_class.dispatch

    def dispatch(self, request, *args, **kwargs):
        user = self.request.user
        print(user)


# Create your views here.
# def modal_registro(request):
#     return render(request, 'modal_registro.html')
def get_fullname_grupo(request):
    user = request.user
    cve = Usuario.objects.get(login=user)
    persona = Persona.objects.get(cve_persona=cve.cve_persona)
    group = group_permission(request, True)
    name = persona.nombre + ' ' + persona.apellido_paterno + ' ' + persona.apellido_materno

    return {
        "group": group,
        "name": name
    }

@login_required
@groups_required('Alumno', 'Docente')
def index_proyectos(request):
    form = estadias_form()
    fullname = get_fullname_grupo(request)['name']
    flag = True
    if get_fullname_grupo(request)['group'] == '27 Docentes':
        flag = False

    reporte = model_estadias.objects.all() if flag else model_estadias.objects.filter(asesor_academico=fullname)
    side_code = 300
    return render(request,'index_proyectos.html',{"reporte":reporte, "form":form,"side_code":side_code})

@login_required
@groups_required('Alumno', 'Docente')
def estadias_registro(request):
    if request.method == 'POST':
        form = estadias_form(request.POST, request.FILES)
        if form.is_valid():
            proyecto = form.cleaned_data['proyecto']
            matricula = form.cleaned_data['matricula']
            alumno = form.cleaned_data['alumno']
            asesor_academico = form.cleaned_data['asesor_academico']
            generacion = form.cleaned_data['generacion']
            empresa = form.cleaned_data['empresa']
            asesor_orga = form.cleaned_data['asesor_orga']
            carrera = form.cleaned_data['carrera']
            name_ref = file_new_name(alumno, form.cleaned_data['reporte_file'].name)

            # Llamado de función para convertir documento a base64
            base64 = convert_base64(form.cleaned_data['reporte_file'])
            fecha_registro = localtime().date()

            proyectos=model_estadias.objects.create(
                    proyecto = proyecto,
                    matricula = matricula,
                    alumno = alumno,
                    asesor_academico = asesor_academico,
                    generacion = generacion,
                    empresa = empresa,
                    asesor_orga = asesor_orga,
                    carrera = carrera,
                    reporte = name_ref,
                    base64 = base64,
                    fecha_registro = fecha_registro
            )
            messages.add_message(request, messages.SUCCESS, 'Registro agregado')
            return redirect('proyectos')
            # return redirect('proyectos')
        else:
            # Si el formulario no es válido, vuelve a renderizar el formulario con errores
            form = estadias_form()
    else:
        form = estadias_form()
        messages.add_message(request, messages.ERROR, '¡Algo salio mal!')
        return redirect('proyectos')

# Función para convertir documento a base64
def convert_base64(doc):
    # Se convierte el pdf en formato base64
    # Lee el documento que llega en formulario
    file = doc.read()
    # Convierte el documento en base64
    encoded_string = base64.b64encode(file)
    return encoded_string.decode('utf-8')

def temporary_file_base_64(base_64_input):
    # base64_string = base_64_input.strip().split(',')[1]
    decoded_bytes = base64.b64decode(base_64_input)
    file_temp, path_temp = tempfile.mkstemp(suffix=".pdf", dir=settings.MEDIA_ROOT + "/")
    try:
        with os.fdopen(file_temp, 'wb') as tmp:
            tmp.write(decoded_bytes)
    except Exception as e:
        os.remove(path_temp)
        raise e
    return path_temp

# Función para mostrar file report
@login_required
@groups_required('Alumno', 'Docente')
def view_report(request, report_rute):
    try:
        # Código de ubicación para sidebar
        side_code = 301
        id_reporte = model_estadias.objects.filter(reporte=report_rute).first()
        # Se crea el archivo temporal y se obtiene la ruta
        name_temp = temporary_file_base_64(id_reporte.base64)
        # Se separan los datos no necesarios
        ruta = name_temp.split('/code')[1]

        return render(request, 'iframe_pdf.html', {'reporte': ruta, "side_code":side_code, "alumno":id_reporte})
    except Exception as v:
        print(f"Error en al generar vista de PDF: {v}")

def insert_consult(request):
    try:
        user_id = request.POST.get('user_id')
        name_reporte = request.POST.get('name_reporte')
        reporte = request.POST.get('id_reporte')

        """ Se registra la consulta en base de datos """
        # estadia = model_estadias.objects.get(id=id_reporte)
        # # Incrementa el número de consultas
        # estadia.consultas = (estadia.consultas or 0) + 1
        # # Actualiza la fecha de consulta a la fecha actual
        # estadia.fecha_consulta = localtime().date()
        # # Guarda los cambios
        # estadia.save()
        """ Fin de guardado """

        if request.method == 'POST':
            id_reporte = reporte
            matricula = user_id
            consultas = 1
            fecha_consulta = localtime().date()

            estadias = register_view.objects.create(
                id_reporte = id_reporte,
                matricula = matricula,
                consultas = consultas,
                fecha_consulta = fecha_consulta
            )
            # messages.add_message(request, messages.SUCCESS, 'Registro agregado')
            # return redirect('estadias')
        # else:
        #     form = estadias_form()
        #     messages.add_message(request, messages.ERROR, '¡Algo salio mal!')
        #     return redirect('estadias')

        # Retorna una respuesta JSON con los datos relevantes
        data = {
            "success": True,
            "message": "Registro actualizado exitosamente.",
            "id": reporte,
            "consultas": consultas,
            "fecha_consulta": fecha_consulta.strftime("%d/%m/%Y"),
        }

        return JsonResponse(data)

    except register_view.DoesNotExist:
        return JsonResponse({"success": False, "message": "El registro no existe."}, status=404)

    except Exception as a:
        # Imprime el error para depuración y devuelve una respuesta de error
        print(f"Algo salió mal: {a}")
        return JsonResponse({"success": False, "message": "Error al procesar la solicitud."}, status=500)

def servir_pdf(request, report_rute):
    file_path = os.path.join(settings.MEDIA_ROOT, report_rute)
    response = FileResponse(open(file_path, 'rb'), content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="mi_documento.pdf"'
    return response

@login_required
@groups_required('Alumno', 'Docente')
# Función de búsqueda para retorno de información por búsqueda con matricula
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
            return JsonResponse(data)
        except Exception as a:
            print(f"Algo salio mal: {a}")
    return JsonResponse({'error': 'Matricula no proporcionada'}, status=400)
