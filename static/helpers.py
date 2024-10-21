import os
from static.utils import dd

def file_new_name(alumno, archivo):
    # Secciona el nombre en un arreglo
    word = alumno.split()
    content = ''
    # Recorre el arreglo y obtiene la primera letra de cada palabra
    for p in word:
        content = content + p[0]
    new_name = content + '_' + archivo

    return new_name