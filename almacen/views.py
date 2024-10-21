from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User
from .models import acervo_model
from .forms import registro_form
from datetime import datetime
from django.contrib import messages
from sito.models import Persona
from sistema.models import UsuarioAcceso, UsuarioManager
from static.helpers import dd

# Create your views here.
def index_acervo(request):
        side_code = 200
        listado = acervo_model.objects.all()
        form = registro_form()
        return render(request, 'index_almacen.html', { "list_acervo": listado, "form":form, "side_code":side_code})

def acervo_registro(request):
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
            fecharegistro = datetime.now()
            fechaedicion = datetime.now()
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
            # Si el formulario no es válido, vuelve a renderizar el formulario con errores
            messages.add_message(request, messages.ERROR, '¡Algo salio mal!')
            return redirect('acervo')
    else:
        form = registro_form()
        messages.add_message(request, messages.ERROR, '¡Algo salio mal!')
        return redirect('acervo')

def delete_acervo(request, col):
        acervo_delete = acervo_model.objects.filter(colocacion=col).first()
        acervo_delete.delete()
        messages.success(request, 'Registro Eliminado')
        return redirect(to="acervo")

def edit_register(request, col):
      register = acervo_model.objects.filter(colocacion=col).first()
      listado = acervo_model.objects.all()
      return redirect(reverse('acervo')+'?'+{"register":register})
      # return redirect(request, 'index_almacen.html', { "id_edit": register, "list_acervo": listado})

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
            acervo_update.fechaedicion = datetime.now()
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