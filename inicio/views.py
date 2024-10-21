from django.shortcuts import render, redirect
from static.utils import dd
from almacen.models import acervo_model
from sito.models import Persona

# Create your views here.
def index_inicio(request):
    # Se asigna el código para el focus en el sidebar
    side_code = 100
    # Se obtienen todos los datos del acervo
    datos = acervo_model.objects.all()
    # Se realiza el conteo de los tipos de formato existentes
    total_book = 0
    format_libro = 0
    format_disco = 0
    for cant in datos:
        if cant.formato == 'book' or cant.formato == 'Libro':
            format_libro += 1
        if cant.formato == 'disc' or cant.formato == 'Disco':
            format_disco += 1
        total_book += cant.cant
    # Obtener el total por estados
    states = []
    EXC = 0
    BUE = 0
    REG = 0
    MAL = 0
    for state in datos:
        if state.estado == 'EXC' or state.estado == 'Excelente':
            EXC += 1
        if state.estado == 'BUE' or state.estado == 'Bueno':
            BUE += 1
        if state.estado == 'REG' or state.estado == 'Regular':
            REG += 1
        if state.estado == 'MAL' or state.estado == 'Malo':
            MAL += 1
    # Se almacenan para el uso de al gráfica
    states.append([EXC,BUE,REG,MAL])
    # Suma total de estados (diferente a la suma de todos los libros)
    total_state = states[0][0] + states[0][1] + states[0][2]
    # Se realiza el recopilado del tipo de adquisición
    t_adqui = []
    name_cole =  []
    for adq in datos:
        ingresa = 'S/D' if adq.adqui == '' else adq.adqui
        t_adqui.append(ingresa)
    # Recorre el arreglo e identifica cuántas veces se repite una elemento
    conteo_adqui = dict(zip(t_adqui, map(lambda x: t_adqui.count(x), t_adqui)))
    value_adqui = []
    for con in conteo_adqui:
        name_cole.append(con)
    for c in range(0, len(name_cole)):
        value_adqui.append(conteo_adqui[name_cole[c]])
    data = {
        "total_book": total_book,
        "states": states[0],
        "total_state": total_state,
        "side_code": side_code,
        "cant_libros":format_libro,
        "cant_discos": format_disco,
        "name_cole": name_cole,
        "value_adqui": value_adqui
    }
    return render(request, 'index_inicio.html', { "data": data })