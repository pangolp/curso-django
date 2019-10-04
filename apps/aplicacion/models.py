from django.db import models


class Curso(models.Model):
    nombre = models.CharField('nombre del curso', max_length=50, 
        help_text='Ingrese el nombre del curso')
    tipo = models.CharField(max_length=50, help_text='ejemplo: computación')
    cantidad_horas = models.PositiveSmallIntegerField('cantidad de horas')

    def __str__(self):
        return 'Curso: %s, Horas: %s' % (self.nombre, self.cantidad_horas)


class Alumno(models.Model):
    dni = models.PositiveSmallIntegerField(unique=True, 
        help_text='Ingrese el dni del alumno')
    apellido = models.CharField(max_length=50, 
        help_text='Ingrese el apellido del alumno')
    nombre = models.CharField(max_length=50, 
        help_text='Ingrese el nombre del alumno')
    observación = models.TextField(blank=True, null=True)
    curso = models.ManyToManyField(Curso)

    def __str__(self):
        return '%s, %s' % (self.apellido, self.nombre)
