from django.shortcuts import render, redirect
from almacen.models import acervo_model
from catalogo.models import model_catalogo
from django.contrib import messages
from .forms import catalogo_form
from django.utils.timezone import now
import json

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
    print("Entra")
    matricula = request.GET.get('matricula')
    print(matricula)
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
            print(data['nombre'])
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

