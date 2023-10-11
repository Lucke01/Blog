Readme de como encare este proyecto personal usando Python y Django

la idea de este blog es que tenga funcionalidades de cargar datos de estudiantes por respectiva materia con profesores y asi...

Paso a paso de como fui encarando el proyecto:

1) una vez creada la App:

a)Modelos: los cree y los registre en la DB

b) Templates: son reciclados de un proyecto de desarrollo web que pude hacer,  Cree views y los registre en el url, Use herencia de Templates para optimizar el tiempo

c) Panel de Administracion: Registro los modelos en admin.py de la app, creo un superuser, usuarios secundarios

d)ApiForms: creando formularios para poder enviar datos a DB a travez de Django.
I) formulario de busqueda 
II) formulario de ingreso de datos de "Materias"
III) formulario de ingreso de datos de "Alumnos"
IV) formulario de ingreso de datos de "Profesor"	