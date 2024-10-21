from django.contrib import admin
from .models import acervo_model
from import_export.admin import ImportExportModelAdmin
from import_export.admin import ImportExportActionModelAdmin
from import_export import resources
from .models import acervo_model
from .forms import registro_form
from django.contrib.auth.admin import UserAdmin

# class acervo_admin(admin.ModelAdmin):
#     list_display = ('titulo','autor','editorial', 'cant','colocacion', 'edicion', 'anio','adqui','estado','formato', 'fecha_registro', 'fecha_edicion')
#     search_fields = ('titulo','colocacion','message')
#     list_filter = ('titulo','colocacion','estado','formato')
#
admin.site.register(acervo_model, ImportExportModelAdmin)

# @admin.register(acervo_model, ImportExportModelAdmin)
# class acervo_admin(UserAdmin):
#     form = registro_form
#
#     list_display = (
#         'titulo','autor','editorial', 'cant','colocacion', 'edicion', 'anio','adqui','estado','formato', 'fecha_registro', 'fecha_edicion'
#         )
#
#     search_fields = ('titulo','colocacion','message')
#     list_filter = ('titulo','colocacion','estado','formato')