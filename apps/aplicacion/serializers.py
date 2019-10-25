from rest_framework import serializers
from .models import Curso, Alumno


class CursoSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Curso
		fields = ('nombre', 'tipo', 'cantidad_horas')


class AlumnoSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = Alumno
		fields = ('dni', 'apellido', 'nombre', 'observación', 'curso')
