from django.db import models
from django.utils.translation import gettext_lazy as _

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
   tipoP = models.CharField(max_length=255, null=True)
   base64 = LongTextField('Portada',null=True,blank=True)
   fechaP = models.DateTimeField(verbose_name='fechaP', null=True)

   def _str_(self):
        return self.prestamos

   class Meta:
        verbose_name="prestamos"
        verbose_name_plural='prestamos'