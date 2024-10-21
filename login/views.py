from django.http import HttpResponse, HttpResponseRedirect, request
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import FormView
from django.contrib.auth import login, logout
from .forms import formularyLogin
from sistema.models import UsuarioAcceso
from django.contrib import messages
# from django.contrib.auth.models import check_password
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

class Login(FormView):
    template_name = 'index_login.html'
    form_class = formularyLogin
    success_url = reverse_lazy('inicio')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            messages.add_message(request, messages.ERROR, 'Por favor introduzca un nombre de usuario y contraseña correctos.')
            return super(Login,self).dispatch(request, *args, **kwargs)

    # def login_view(request):
    #     if request.user.is_authenticated:
    #         return redirect('inicio')
    #     form = formularyLogin(request.POST or None) # Instanciar el formulario
#
    #     if request.method == 'POST':
    #         if form.is_valid():
    #             login = form.cleaned_data['username']
    #             password = form.cleaned_data['password']
#
    #             sistema_usuario = UsuarioAcceso.objects.filter(login=login).first()
    #             # Si el usuario existe en sistema_usuario, intentamos autenticarlo
    #             if check_password(password, sistema_usuario.password):
    #                 usuario = authenticate(request, username=login, password=password)
    #                 if usuario is not None:
    #                     auth_login(request, usuario)
    #                     if 'next' in request.GET:
    #                         return redirect(request.GET['next'])
    #                     return redirect('usuario:login')
    #                 else:
    #                     messages.add_message(request, messages.ERROR, 'Por favor introduzca un nombre de usuario y contraseña correctos.')
    #                     return HttpResponseRedirect('/accounts/login/')
    #             else:
    #                 messages.add_message(request, messages.ERROR, 'La contraseña que ingresaste es incorrecta.')
    #                 return HttpResponseRedirect('/accounts/login/')
    #         else:
    #             # El usuario no existe en sistema_usuario, buscar en Usuario
    #             usuario_existente = Usuario.objects.filter()


    def form_valid(self, form):
        login(self.request,form.get_user())
        return super(Login,self).form_valid(form)

def logoutUser(request):
    logout(request)
    return HttpResponseRedirect('/accounts/login/')