from django import forms


#---------------------------------MATERIA_FORMULARIO--------------------
class MateriaFormulario(forms.Form):
    #especificando campos
    nombre = forms.CharField(max_length=30)
    comision = forms.IntegerField()
#---------------------------------ALUMNO_FORMULARIO--------------------
class AlumnoFormulario(forms.Form):
    #especificando campos
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    año = forms.IntegerField(max_value=5)
    carrera = forms.CharField(max_length=30)
    
    

##---------------------------------PROFESOR_FORMULARIO--------------------
class ProfesorFormulario(forms.Form):
    #especificando campos
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    asignatura = forms.CharField(max_length=20)