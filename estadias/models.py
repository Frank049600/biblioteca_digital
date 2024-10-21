from typing import Any
from django.db import models
# from django_mysql.models import LongTextField

class LongTextField(models.TextField):
    def db_type(self, connection):
        if connection.vendor == 'mysql':
            return 'LONGTEXT'
        return super().db_type(connection)
class model_estadias(models.Model):

   proyecto=models.CharField(max_length=255)
   matricula=models.IntegerField()
   alumno=models.CharField(max_length=255)
   asesor_academico=models.CharField(max_length=255)
   generacion=models.CharField(max_length=255)
   empresa=models.CharField(max_length=255)
   asesor_orga=models.CharField(max_length=255)
   ELECCION_CARRERA = (
        ("ADC","ADC"),
        ("MET", "MET"),
        ("QAI", "QAI"),
        ("PIA", "PIA"),
        ("QAM", "QAM"),
        ("ERC","ERC"),
        ("IDGS","IDGS"),
        ("ITEA","ITEA"),
        ("IMET","IMET"),
        ("IER","IER"),
        ("ISIP","ISIP"),
        ("IPQ","IPQ"),
        ("LGCH","LGCH"))
   carrera=models.CharField(max_length=20)
   # reporte = models.FileField('Reporte',null=True,blank=True)
   reporte=models.CharField(max_length=255,null=True)
   base64 = LongTextField('Reporte',null=True,blank=True)

   def _str_(self):
        return self.alumno

   class Meta:
        verbose_name="estadía"
        verbose_name_plural='estadías'

