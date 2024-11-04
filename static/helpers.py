import os
from static.utils import dd
from django.utils.decorators import method_decorator
# from sito.models import groups_list
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect
from django.contrib import messages

def file_new_name(alumno, archivo):
    # Secciona el nombre en un arreglo
    word = alumno.split()
    content = ''
    # Recorre el arreglo y obtiene la primera letra de cada palabra
    for p in word:
        content = content + p[0]
    new_name = content + '_' + archivo

    return new_name

# def add_group_name_to_context(view_class):
#     original_dispatch = view_class.dispatch
#
#     def dispatch(self, request, *arg, **kwargs):
#         user = self.request.user

def groups_required(*group_names):
    """Decorador para restringir el acceso a usuarios que pertenezcan a uno de varios grupos."""
    def decorator(view_func):
        @login_required
        def _wrapped_view(request, *args, **kwargs):
            # Verificar si el usuario pertenece a al menos uno de los grupos
            if request.user.groups.filter(name__in=group_names).exists():
                return view_func(request, *args, **kwargs)
            else:
                messages.add_message(request, messages.INFO, 'No tienes permisos para entrar')
                return redirect('inicio')
        return _wrapped_view
    return decorator