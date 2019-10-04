from django.urls import include, path
from rest_framework import routers
from .views import CursoViewSet, AlumnoViewSet


router = routers.DefaultRouter()
router.register('curso', CursoViewSet)
router.register('alumno', AlumnoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
