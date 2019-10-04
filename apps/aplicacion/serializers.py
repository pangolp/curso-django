from rest_framework import serializers
from .models import Curso, Alumno


class CursoSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Curso
		fields = ('id', 'nombre', 'tipo', 'cantidad_horas', 'url')


class AlumnoSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Alumno
		fields = ('id', 'dni', 'apellido', 'nombre', 'observación', 'curso', 'url')
