from django.urls import path
from Blog_app import views


urlpatterns = [
    path("",views.inicio, name = "Inicio"), #pagina inicio
    path("alumno",views.alumno, name = "Alumno"),
    path("materia",views.materia, name = "Materia"),
    path("profesor",views.profesor, name = "Profesor"),
    path("busquedas",views.busquedas, name= "Busquedas"),
    path("buscar/",views.buscar)

]
   