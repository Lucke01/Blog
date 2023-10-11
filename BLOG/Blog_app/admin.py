from django.contrib import admin

# Register your models here.


from .models import *

admin.site.register(Materia)
admin.site.register(Alumno)
admin.site.register(Profesor)

