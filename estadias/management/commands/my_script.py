from django.core.management.base import BaseCommand
from estadias.tem_delete import borrar_archivos_pdf

class Command(BaseCommand):
    help = 'Descripción del comando'

    def handle(self, *args, **kwargs):
        # Coloca aquí el código que deseas ejecutar
        print("Ejecutando el script personalizado")
        borrar_archivos_pdf()