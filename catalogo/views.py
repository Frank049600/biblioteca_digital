from django.shortcuts import render
from static.helpers import *

# Create your views here.
@groups_required('Administrador', 'Docente', 'Alumno')
def catalago_View(request):
    side_code = 400
    return render(request, 'index_catalogo.html', {"side_code": side_code})
