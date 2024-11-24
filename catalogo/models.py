from django.db import models
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

   def _str_(self):
        return self.prestamos

   class Meta:
        verbose_name="prestamos"
        verbose_name_plural='prestamos'