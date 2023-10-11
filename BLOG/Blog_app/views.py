from django.shortcuts import render
from django.http import HttpResponse
from Blog_app.models import Materia,Alumno,Profesor
from Blog_app.forms import MateriaFormulario,ProfesorFormulario,AlumnoFormulario

# Create your views here.
#--------------------------------- INICIO.html -------------------------------------------------
def inicio(request):
    return render(request, "Blog_app/Inicio.html")


#--------------------------------- MATERIA.html -------------------------------------------------
def materia(request):
    
    #creando el formulario
    if request.method == 'POST':
        miFormulario= MateriaFormulario(request.POST) #aca llega la info del html

        print(miFormulario) 

        if miFormulario.is_valid():

            info = miFormulario.cleaned_data

            m = Materia(nombre = info['nombre'],comision = info['comision'])

            m.save()

            return render(request, 'Blog_app/inicio.html')
        
    else:

            miFormulario=MateriaFormulario() #form vacio

    return render(request,'Blog_app/materia.html',{"miFormulario":miFormulario})

#--------------------------------- ALUMNO.html -------------------------------------------------
def alumno(request):
    if request.method == 'POST':
        #creo el formulario
        alumnoForm = AlumnoFormulario(request.POST)

        print(alumnoForm)

        #sigo definiendo el formulario desde la db
        if alumnoForm.is_valid():

            #creo los campos del formulario
            informacion = alumnoForm.cleaned_data

            alumno = Alumno(nombre = informacion['nombre'], apellido = informacion['apellido'],año = informacion['año'],carrera = informacion['carrera']) 
            
            alumno.save()
            
            return render(request, 'Blog_app/inicio.html')
    else:
        
        alumnoForm = AlumnoFormulario()
    
    return render(request, 'Blog_app/alumno.html',{"alumnoForm":alumnoForm})


#--------------------------------- PROFESOR.html -------------------------------------------------
def profesor(request):
    if request.method == 'POST':
       
        profeForm = ProfesorFormulario(request.POST)

        print(profeForm)

        if profeForm.is_valid():
           
           i = profeForm.cleaned_data

           profesor = Profesor(nombre = i['nombre'], apellido = i['apellido'],asignatura =i['asignatura'])

           profesor.save()

           return render(request, 'Blog_app/inicio.html')
       
    else: 
           
           profeForm = ProfesorFormulario()
        
    return render(request, 'Blog_app/profesor.html', {"profeForm":profeForm})

#----------------------------------- BUSCAR--------------------------
def buscar(request):
    if request.GET["comision"]:
        comision = request.GET['comision']
        materia = Materia.objects.filter(comision__icontains = comision)
        return render(request, "Blog_app/busquedas.html",{'materia':materia, 'comision':comision})
    else:
        rta = "usted no cargo los datos"
    return render(request, 'Blog_app/busquedas.html',{"rta":rta})

#--------------------------------------busquedas.html----------------------------------------------

def busquedas(request):
    return render(request, "Blog_app/busquedas.html")
