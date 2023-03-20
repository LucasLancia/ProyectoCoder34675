from django.shortcuts import render, redirect
from AppCoder.models import Curso,Estudiante,Profesor
from AppCoder.forms import CursoForms, BusquedaCursoForms, BusquedaProfesorForms, BusquedaAlumnoForms,ProfesorFormulario, AlumnoFormulario


def busqueda_curso(request):
    mi_formulario = BusquedaCursoForms(request.GET)
    if mi_formulario.is_valid():
        informacion = mi_formulario.cleaned_data
        cursos_filtrados = Curso.objects.filter(nombre__icontains=informacion['nombre'])
        context = {
            "cursos": cursos_filtrados
        }
    return render(request, "AppCoder/busqueda_curso.html", context=context)


def cursos(request):
    if request.method == "POST":
        mi_formulario = CursoForms(request.POST)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            curso_save = Curso(
                nombre=informacion['nombre'],
                camada=informacion['camada']

            )
            curso_save.save()

    all_cursos = Curso.objects.all()
    context = {
        "cursos": all_cursos,
        "form": CursoForms(),
        "form_busqueda": BusquedaCursoForms(),
    }
    return render(request, "AppCoder/cursos.html", context=context)


def crear_curso(request, nombre, camada):
    save_curso = Curso(nombre=nombre, camada=int(camada))
    save_curso.save()
    context = {
        "nombre": nombre,
        "camada": camada
    }
    return render(request, "AppCoder/save_curso.html", context)


def estudiantes(request):
    if request.method == "POST":
        mi_formulario = AlumnoFormulario(request.POST)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            estudiante_save = Estudiante(
                nombre=informacion['nombre'],
                apellido=informacion['apellido'],
                ##telefono=informacion['telefono'],
                email=informacion['email']

            )
            estudiante_save.save()

    all_estudiantes = Estudiante.objects.all()
    context = {
        "estudiante": all_estudiantes,
        "form": AlumnoFormulario(),
        "form_busqueda": BusquedaAlumnoForms(),
    }
    return render(request, "AppCoder/estudiantes.html", context=context)


def profesores(request):
    if request.method == "POST":
        mi_formulario = ProfesorFormulario(request.POST)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            profesor_save = Profesor(
                nombre=informacion['nombre'],
                apellido=informacion['apellido'],
                ##telefono=informacion['telefono'],
                email=informacion['email'],
                profesion=informacion['profesion']

            )
            profesor_save.save()

    all_profesor = Profesor.objects.all()
    context = {
        "profesor": all_profesor,
        "form": ProfesorFormulario(),
        "form_busqueda": BusquedaProfesorForms(),
    }
    return render(request, "AppCoder/profesores.html", context=context)


def busqueda_alumno(request):
    mi_formulario = BusquedaAlumnoForms(request.GET)
    if mi_formulario.is_valid():
        informacion = mi_formulario.cleaned_data
        alumnos_filtrados = Alumno.objects.filter(nombre__icontains=informacion['nombre'])
        context = {
            "alumno": alumnos_filtrados
        }
    return render(request, "AppCoder/busqueda_estudiante.html", context=context)


def busqueda_profesor(request):
    mi_formulario = BusquedaProfesorForms(request.GET)
    if mi_formulario.is_valid():
        informacion = mi_formulario.cleaned_data
        profesor_filtrados = profesor.objects.filter(nombre__icontains=informacion['nombre'])
        context = {
            "profesor": profesor_filtrados
        }
    return render(request, "AppCoder/busqueda_profesor.html", context=context)

def crear_estudiante(request, nombre,apellido,email):
    save_estudiante = Estudiante(nombre=nombre,apellido=apellido,email=email)
    save_estudiante.save()
    context = {
        "nombre": nombre,
        "apellido":apellido,
        "email":email
    }
    return render(request, "AppCoder/save_estudiante.html", context)

def crear_profesor(request, nombre,apellido,email,profesion):
    save_profesor = profesor(nombre=nombre,apellido=apellido,email=email,profesion=profesion)
    save_profesor.save()
    context = {
        "nombre": nombre,
        "apellido":apellido,
        ##"telefono":telefono,
        "email":email,
        "profesion":profesion
    }
    return render(request, "AppCoder/save_profesor.html", context)