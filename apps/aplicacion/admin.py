from django.contrib import admin
from .models import Curso, Alumno


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo', 'cantidad_horas')
    list_filter = ('tipo',)
    search_fields = ['nombre', 'tipo', 'cantidad_horas']


@admin.register(Alumno)
class AlumnoAdmin(admin.ModelAdmin):
    list_display = ('apellido', 'nombre', 'dni')
    list_filter = ('curso',)
    search_fields = ['apellido', 'nombre', 'dni']
