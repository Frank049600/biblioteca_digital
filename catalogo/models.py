from django.db import models
from django.utils.translation import gettext_lazy as _

# from django_mysql.models import LongTextField

class LongTextField(models.TextField):
    def db_type(self, connection):
        if connection.vendor == 'mysql':
            return 'LONGTEXT'
        return super().db_type(connection)
class model_catalogo(models.Model):

   nom_libro=models.CharField(max_length=255)
   nom_autor=models.CharField(max_length=255)
   edicion=models.CharField(max_length=255)
   colocacion=models.CharField(max_length=255)
   cantidad=models.IntegerField()
   matricula=models.IntegerField()
   nom_alumno=models.CharField(max_length=255)
   carrera_grupo=models.CharField(max_length=255)
   tipoP = models.CharField(max_length=5, null=True)
   fechaP = models.DateTimeField(verbose_name='fechaP', null=True)
   #tipoP = models.CharField(max_length=5, verbose_name="Tipo de Prestamo", choices=format.choices, default=format.EXTERNO, null=True, blank=True)

   def _str_(self):
        return self.prestamos

   class Meta:
        verbose_name="prestamos"
        verbose_name_plural='prestamos'