# estadias/management/commands/my_script.py

# from django.core.management.base import BaseCommand
# from estadias import tem_delete  # Asegúrate de que el script esté en esta ruta
#
# class Command(BaseCommand):
#     help = 'Ejecuta el script mi_script.py dentro de estadias'
#
#     def handle(self, *args, **kwargs):
#         print('Al menos llega')
#         # Aquí llama a las funciones que quieres ejecutar en el script
#         tem_delete.borrar_archivos_pdf()  # Ajusta según tu script


# management/commands/my_script.py

from django.core.management.base import BaseCommand
from estadias.tem_delete import borrar_archivos_pdf

class Command(BaseCommand):
    help = 'Descripción del comando'

    def handle(self, *args, **kwargs):
        # Coloca aquí el código que deseas ejecutar
        print("Ejecutando el script personalizado")
        borrar_archivos_pdf()