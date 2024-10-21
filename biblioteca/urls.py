from django.contrib import admin
from django.urls import path, include, re_path
from almacen.views import index_acervo as acervo
from almacen.views import acervo_registro, delete_acervo, edit_register, edit_acervo
from inicio.views import index_inicio as inicio
from estadias.views import index_proyectos as proyectos
from django.contrib.auth.decorators import login_required
from login.views import Login, logoutUser
from estadias.views import estadias_registro
from estadias.views import view_report, servir_pdf, get_alumno
from usuario.views import login_view
from catalogo.views import catalago_View
#
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls, name = 'panel'),
    path('acervo/', login_required(acervo), name = 'acervo'),
    path('', login_required(inicio), name = 'inicio'),
    # path('accounts/login/', Login.as_view(), name = 'login'),
    path('accounts/login/', login_view, name = 'login'),
    path('logout/', login_required(logoutUser), name = 'logout'),
    path('proyectos/',login_required(proyectos),name='proyectos'),
    # Rutas de registro Acervo
    path('acervo_registro/', login_required(acervo_registro), name='acervo_registro'),
    path('delete_acervo/<col>', login_required(delete_acervo), name='delete_acervo'),
    path('edit_register/<col>', login_required(edit_register), name='edit_register'),
    path('edit_acervo/', login_required(edit_acervo), name='edit_acervo'),
    # path('deleteAcervo/<codigo>', deleteAcervo)

    path('estadias_registro/',login_required(estadias_registro)),
    path('get_alumno/', get_alumno, name='get_alumno'),

    path('view_report/<report_rute>', login_required(view_report), name='view_report'),
     path('view_report/<report_rute>', login_required(servir_pdf), name='servir_pdf'),

    # aplicación de sesión
    path('session-security/', include('session_security.urls')),

    # Aplicación de catalogo
    path('catalago_View', login_required(catalago_View), name='catalago_View'),
]

urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT,
    })
]
