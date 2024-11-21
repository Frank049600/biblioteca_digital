import json
from django.shortcuts import render, redirect
from almacen.models import acervo_model

def csv():
    data = acervo_model.objects.all()
    
    t = {}
    t2 = []
    cont = 1
    cont2 = 0
    sum = {}
    for titulo in data:
        t2.append(titulo.titulo)
        t[cont] = titulo.titulo
        cont += 1

    print(len(t))
    
    total = 0
    for cant in data:
        total += cant.cant 

    print(total)
    # for i in range(1, len(t)):
    #     if t[i] in t2:
    #         sum[cont2] = t[i]
    #         cont2 += 1

    # print(json.dumps(t, sort_keys=True, ensure_ascii=True, indent=2))