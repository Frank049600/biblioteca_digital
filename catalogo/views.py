from django.shortcuts import render

# Create your views here.
def catalago_View(request):
    side_code = 400
    return render(request, 'index_catalogo.html', {"side_code": side_code})
