from django import forms
from .models import model_catalogo

class catalogo_form(forms.ModelForm):

    format = [
            ('ext','Externo'),
            ('inter','Interno')
            ]

    nom_libro = forms.CharField(label='Nombre del libro', required=True, max_length=255, widget=forms.TextInput (attrs={'class':'form-control','placeholder':'Ingrese el nombre del libro', 'readonly':True}))
    nom_autor = forms.CharField(label='Nombre del autor', required=False, max_length=255, widget=forms.TextInput (attrs={'class':'form-control','placeholder':'Ingrese el nombre del autor', 'readonly':True}))
    edicion = forms.CharField(label='Edición', required=False, max_length=255, widget=forms.TextInput (attrs={'class':'form-control','placeholder':'Edición', 'readonly':True}))
    colocacion = forms.CharField(label='Colocación', required=True, max_length=255, widget=forms.TextInput (attrs={'class':'form-control','placeholder':'Colocación', 'readonly':True}))
    cantidad = forms.IntegerField(label='Cantidad', required=True, widget=forms.NumberInput (attrs={'class':'form-control','placeholder':'Cantidad de libros prestados'}))
    matricula = forms.IntegerField(label='Matricula', required=True, widget=forms.NumberInput (attrs={'class':'form-control','placeholder':'Ingrese la matricula del alumno', 'readonly':True}))
    nom_alumno = forms.CharField(label='Nombre del alumno', required=True, max_length=255, widget=forms.TextInput (attrs={'class':'form-control','placeholder':'Ingrese el nombre del alumno', 'readonly':True}))
    carrera_grupo = forms.CharField(label='Carrera', required=True, max_length=255, widget=forms.TextInput (attrs={'class':'form-control','placeholder':'Ingrese la carrera y grupo del alumno', 'readonly':True}))
    tipoP = forms.ChoiceField(label='Tipo de Prestamo', choices=format, required=True, widget=forms.Select (attrs={'class':'form-control', 'placeholder':'Seleccione tipo de prestamo'}))

    class Meta:
        model = model_catalogo
        fields = ('nom_libro', 'nom_autor', 'edicion' ,'colocacion', 'cantidad', 'matricula', 'nom_alumno', 'carrera_grupo', 'tipoP')