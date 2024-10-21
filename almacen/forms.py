from django import forms
from .models import acervo_model

class registro_form(forms.ModelForm):

    state = [
            ('EXC','Excelente'),
            ('BUE','Bueno'),
            ('REG','Regular'),
            ('MAL','Malo')
            ]
    format = [
            ('book','Libro'),
            ('disc','Disco')
            ]

    titulo = forms.CharField(label='Titulo', required=True, max_length=100, widget=forms.TextInput (attrs={'class':'form-control','placeholder':'Ingrese el titulo'}))
    autor = forms.CharField(label='Autor', required=False, max_length=100, widget=forms.TextInput (attrs={'class':'form-control','placeholder':'Ingrese el autor'}))
    editorial = forms.CharField(label='Editorial', required=False, max_length=100, widget=forms.TextInput (attrs={'class':'form-control','placeholder':'Ingrese la editorial'}))
    cant = forms.IntegerField(label='Cantidad', required=True, widget=forms.NumberInput (attrs={'class':'form-control','placeholder':'Indique la cantidad de libros'}))
    colocacion = forms.CharField(label='Colocación', required=True, max_length=100, widget=forms.TextInput (attrs={'class':'form-control','placeholder':'Ingrese la colocacion'}))
    edicion = forms.CharField(label='Edición', required=False, max_length=100, widget=forms.TextInput (attrs={'class':'form-control','placeholder':'Ingrese la edición'}))
    anio = forms.IntegerField(label='Año', required=False, widget=forms.NumberInput (attrs={'class':'form-control','placeholder':'Ingrese el año de edición'}))
    adqui = forms.CharField(label='Tipo de adquisición', required=False, max_length=100, widget=forms.TextInput (attrs={'class':'form-control','placeholder':'indique el tipo de adquisición'}))
    formato = forms.ChoiceField(label='Formato', choices=format, required=True, widget=forms.Select (attrs={'class':'form-control','placeholder':'Indique el formato del libro'}))
    estado = forms.ChoiceField(label='estado', choices=state, required=True, widget=forms.Select (attrs={'class':'form-control','placeholder':'Indique el estado del libro'}))
    class Meta:
        model = acervo_model
        fields = ('titulo','autor','editorial','cant','colocacion','edicion','anio','adqui','formato','estado')