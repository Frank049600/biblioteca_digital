
import time
import schedule
import os
from django.conf import settings
from datetime import datetime
import math
import pytz

# Función para el vaciado de la carpeta
def borrar_archivos_pdf():
    carpeta = settings.MEDIA_ROOT
    for archivo in os.listdir(carpeta):
        if archivo.endswith('.pdf'):
            os.remove(os.path.join(carpeta, archivo))
            print(f'Archivo borrado: {archivo}')

# if __name__ == '__main__':
# Programar la tarea para que se ejecute una vez al día
# schedule.every(24).hours.do(borrar_archivos_pdf)
# schedule.every(1).minutes.do(borrar_archivos_pdf)


def calcular_diferencia(tiempo_inicio, tiempo_fin):
    formato_hora = "%I:%M:%S"
    t1 = datetime.strptime(tiempo_inicio, formato_hora)
    t2 = datetime.strptime(tiempo_fin, formato_hora)
    diferencia = t2 - t1
    total_minutos = diferencia.total_seconds() / 60
    return redondear_a_dos_decimales(total_minutos)

def redondear_a_dos_decimales(valor):
    valor_redondeado = math.floor(valor * 100) / 100
    if valor_redondeado % 1 >= 0.59:
        return math.ceil(valor_redondeado)
    else:
        return valor_redondeado

def comparación():
    # Configura la zona horaria deseada
    zona_horaria = pytz.timezone("America/Mexico_City")
    tiempo_inicio = "12:00:00"
    tiempo_fin = datetime.now(zona_horaria).time().strftime("%I:%M:%S")

    # 1 día = 1440
    # resultado = calcular_diferencia(tiempo_inicio, tiempo_fin)
    print('entra')
    print("Diferencia en minutos:", resultado)
    print(resultado, '309.26')
    if resultado >= 309.26:
        print('entra')
        # borrar_archivos_pdf()

# while True:
#     schedule.every(1).minutes.do(comparación)
#     schedule.run_pending()
#     # time.sleep(1)  # Esperar un segundo entre verificaciones