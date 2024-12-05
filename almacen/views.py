from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User
from .models import acervo_model
from .forms import registro_form
from datetime import datetime
from django.contrib import messages
from sito.models import Persona
from sistema.models import UsuarioAcceso, UsuarioManager
from static.helpers import *
from django.utils.timezone import now

# Create your views here.
@groups_required('Administrador')
def index_acervo(request):
        side_code = 200
        listado = acervo_model.objects.all()
        form = registro_form()
        return render(request, 'index_almacen.html', { "list_acervo": listado, "form":form, "side_code":side_code})

@groups_required('Administrador')
def acervo_registro(request):
    try:
        if request.method == 'POST':
            form = registro_form(request.POST)
            if form.is_valid():
                titulo = form.cleaned_data['titulo']
                autor = form.cleaned_data['autor']
                editorial = form.cleaned_data['editorial']
                cant = form.cleaned_data['cant']
                colocacion = form.cleaned_data['colocacion']
                edicion = form.cleaned_data['edicion']
                anio = form.cleaned_data['anio']
                adqui = form.cleaned_data['adqui']
                formato = form.cleaned_data['formato']
                estado = form.cleaned_data['estado']
                fecharegistro = now().replace(microsecond=0)
                fechaedicion = now().replace(microsecond=0)
                
                # Validar si no se repide la colocación
                coloca_exist = acervo_model.objects.filter(colocacion=form.cleaned_data['colocacion'])
                if coloca_exist:
                    messages.add_message(request, messages.INFO, '¡La colocación no puede repetirse!')
                    return redirect('acervo')
                acervo = acervo_model.objects.create(
                        titulo = titulo,
                        autor = autor,
                        editorial = editorial,
                        cant = cant,
                        colocacion = colocacion,
                        edicion = edicion,
                        anio = anio,
                        adqui = adqui,
                        formato = formato,
                        estado = estado,
                        fecharegistro = fecharegistro,
                        fechaedicion = fechaedicion
                )
                messages.add_message(request, messages.SUCCESS, 'Registro agregado')
                return redirect('acervo')
            else:
                print(form.error)
                # Si el formulario no es válido, vuelve a renderizar el formulario con errores
                messages.add_message(request, messages.ERROR, '¡Algo esta mal con el formulario!')
                return redirect('acervo')
        else:
            form = registro_form()
            messages.add_message(request, messages.ERROR, '¡Algo salio mal con el traslado de información!')
            return redirect('acervo')
    except Exception as e:
        messages.add_message(request, messages.ERROR, '¡Algo salio mal!')
        return redirect('acervo')


@groups_required('Administrador')
def delete_acervo(request, col):
        acervo_delete = acervo_model.objects.filter(colocacion=col).first()
        acervo_delete.delete()
        messages.success(request, 'Registro Eliminado')
        return redirect(to="acervo")

@groups_required('Administrador')
def edit_register(request, col):
    print(col)
    register = acervo_model.objects.filter(colocacion=col).first()
    listado = acervo_model.objects.all()
    return redirect(reverse('acervo')+'?'+{"register":register})
    # return redirect(request, 'index_almacen.html', { "id_edit": register, "list_acervo": listado})

@groups_required('Administrador')
def edit_acervo(request):
    if request.method == 'POST':
        form = registro_form(request.POST)
        if form.is_valid():
            acervo_update = acervo_model.objects.filter(colocacion=form.cleaned_data['colocacion']).first()
            acervo_update.titulo = form.cleaned_data['titulo']
            acervo_update.autor = form.cleaned_data['autor']
            acervo_update.editorial = form.cleaned_data['editorial']
            acervo_update.cant = form.cleaned_data['cant']
            acervo_update.colocacion = form.cleaned_data['colocacion']
            acervo_update.edicion = form.cleaned_data['edicion']
            acervo_update.anio = form.cleaned_data['anio']
            acervo_update.adqui = form.cleaned_data['adqui']
            acervo_update.estado = form.cleaned_data['estado']
            acervo_update.formato = form.cleaned_data['formato']
            acervo_update.fechaedicion = now().replace(microsecond=0)
            # Valida que la colocación no se repita
            coloca_exist = acervo_model.objects.exclude(id=acervo_update.id).filter(colocacion=form.cleaned_data['colocacion']).first()
            if coloca_exist:
                messages.add_message(request, messages.INFO, '¡La colocación no puede repetirse!')
                return redirect('acervo')                
            acervo_update.save()
            # Muestra un mensaje de éxito si no existe un problema
            # Retorna hacia Acervo
            messages.add_message(request, messages.SUCCESS, 'Registro actualizado')
            return redirect('acervo')
        else:
            # Si el formulario no es válido, vuelve a renderizar el formulario con errores
            form = registro_form()
            messages.add_message(request, messages.ERROR, '¡Algo salio mal!')
            return redirect('acervo')
    else:
        form = registro_form()
        messages.add_message(request, messages.ERROR, '¡Algo salio mal!')
        return redirect('acervo')