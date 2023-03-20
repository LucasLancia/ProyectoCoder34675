from django import forms


class AlumnoFormulario(forms.Form):
    nombre=forms.CharField(max_length=15)
    apellido=forms.CharField(max_length=15)
    ##telefono=forms.CharField(max_length=15)
    email=forms.CharField(max_length=40)

class ProfesorFormulario(forms.Form):
    nombre=forms.CharField(max_length=15)
    apellido=forms.CharField(max_length=15)
    ##telefono=forms.CharField(max_length=15)
    email=forms.CharField(max_length=40)
    profesion=forms.CharField(max_length=40)

class CursoForms(forms.Form):
    nombre=forms.CharField(min_length=3,max_length=20)
    camada=forms.IntegerField()


class BusquedaCursoForms(forms.Form):
    nombre=forms.CharField(min_length=3,max_length=20)


class BusquedaAlumnoForms(forms.Form):
    nombre = forms.CharField(min_length=3, max_length=20)
    apellido = forms.CharField(max_length=15)

class BusquedaProfesorForms(forms.Form):
    nombre = forms.CharField(min_length=3, max_length=20)
    apellido = forms.CharField(max_length=15)