from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class acervo_model(models.Model):
    class state(models.TextChoices):
        EXCELENTE = 'EXC', _('Excelente')
        BUENO = 'BUE', _('Bueno')
        REGULAR = 'REG', _('Regular')
        MALO = 'MAL', _('Malo')

    class format(models.TextChoices):
        LIBRO = 'book', _('Libro')
        DISCO = 'disc', _('Disco')

    titulo = models.CharField(max_length=100,verbose_name="titulo", null=True, blank=True)
    autor = models.CharField(max_length=100,verbose_name="Autor", null=True, blank=True)
    editorial = models.CharField(max_length=100,verbose_name="Editorial", null=True, blank=True)
    cant = models.IntegerField(verbose_name="Cantidad", null=True, blank=True)
    colocacion = models.CharField(max_length=100,verbose_name="Colocación", null=True, blank=True)
    edicion = models.CharField(max_length=100, verbose_name="Edición", null=True, blank=True)
    anio = models.CharField(max_length=20,verbose_name="Año de edición", null=True, blank=True)
    adqui = models.CharField(max_length=20,verbose_name="Tipo de adquisición", null=True, blank=True)
    estado = models.CharField(max_length=3, verbose_name="Estado", choices=state.choices, default=state.EXCELENTE, null=True, blank=True)
    formato = models.CharField(max_length=5, verbose_name="formato", choices=format.choices, default=format.LIBRO, null=True, blank=True)
    fecharegistro = models.DateField(verbose_name="Fecha de Registro", null=True, blank=True)
    fechaedicion = models.DateField(verbose_name="Fecha de actualización", null=True, blank=True)

    def _str_(self):
        return self.titulo

    class Meta:
        verbose_name = 'Acervo registros'