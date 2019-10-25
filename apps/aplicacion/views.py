from rest_framework import viewsets, filters
from .serializers import CursoSerializer, AlumnoSerializer
from .models import Curso, Alumno


class CursoViewSet(viewsets.ModelViewSet):
	queryset = Curso.objects.all()
	serializer_class = CursoSerializer


class AlumnoViewSet(viewsets.ModelViewSet):
	search_fields = ['apellido', 'nombre', 'dni']
	filter_backends = (filters.SearchFilter, )
	queryset = Alumno.objects.all()
	serializer_class = AlumnoSerializer
