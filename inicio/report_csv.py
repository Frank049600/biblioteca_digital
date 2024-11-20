import json
from django.shortcuts import render, redirect
from almacen.models import acervo_model

def csv():
    data = acervo_model.objects.all()
    print(data)