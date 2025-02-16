from django.urls import path
from .views import itineraire_course, itineraire_velo, itineraire_randonnee, itineraire_fitness, itineraire_course_groupe, itineraire_marche_recuperation

urlpatterns = [
    path('itineraire-course/', itineraire_course, name='itineraire-course'),
    path('itineraire-velo/', itineraire_velo, name='itineraire-velo'),
    path('itineraire-randonnee/', itineraire_randonnee, name='itineraire-randonnee'),
    path('itineraire-fitness/', itineraire_fitness, name='itineraire-fitness'),
    path('itineraire-course-groupe/', itineraire_course_groupe, name='itineraire-course-groupe'),
    path('itineraire-marche-recuperation/', itineraire_marche_recuperation, name='itineraire-marche-recuperation'),
]
