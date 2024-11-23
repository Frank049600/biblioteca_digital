from django.shortcuts import render, redirect
from almacen.models import acervo_model
from catalogo.models import model_catalogo
from django.contrib import messages
from .forms import catalogo_form

# Create your views here.
def catalago_View(request):
    form = catalogo_form()
    side_code = 400
    listado = acervo_model.objects.all()
    return render(request, 'index_catalogo.html', {"side_code": side_code, "listado":listado, "form":form})

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
        if form.is_valid():
            nom_libro = form.cleaned_data['nom_libro']
            nom_autor = form.cleaned_data['nom_autor']
            edicion = form.cleaned_data['edicion']
            colocacion = form.cleaned_data['colocacion']
            cantidad = form.cleaned_data['cantidad']
            matricula = form.cleaned_data['matricula']
            nom_alumno = form.cleaned_data['nom_alumno']
            carrera_grupo = form.cleaned_data['carrera_grupo']

            catalago_View=model_catalogo.objects.create(
                    nom_libro = nom_libro,
                    nom_autor = nom_autor,
                    edicion = edicion,
                    colocacion = colocacion,
                    cantidad = cantidad,
                    matricula = matricula,
                    nom_alumno = nom_alumno,
                    carrera_grupo = carrera_grupo
            )
            messages.add_message(request, messages.SUCCESS, 'Prestamo Solicitado')
            return redirect('catalago_View')
            # return redirect('proyectos')
        else:
            # Si el formulario no es válido, vuelve a renderizar el formulario con errores
            form = catalogo_form()
    else:
        form = catalogo_form()
        messages.add_message(request, messages.ERROR, '¡Algo salio mal!')
        return redirect('catalago_View')

