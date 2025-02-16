import requests
from rest_framework.response import Response
from rest_framework.decorators import api_view


CLE_API_OPENROUTEUR = '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'
URL_API_OPENROUTEUR = 'https://api.openrouteservice.org/v2/directions/'

def requete_openrouteur(profil, coordonnees):
    en_tetes = {
        'Authorization': f'Bearer {CLE_API_OPENROUTEUR}',
        'Content-Type': 'application/json'
    }
    donnees = {
        "locations": coordonnees,
        "profile": profil
    }
    reponse = requests.post(URL_API_OPENROUTEUR + profil + "/json", json=donnees, headers=en_tetes)
    return reponse.json()

@api_view(['POST'])
def itineraire_course(request):
    coordonnees = request.data.get('locations')
    reponse = requete_openrouteur('foot-walking', coordonnees)
    return Response(reponse)

@api_view(['POST'])
def itineraire_velo(request):
    coordonnees = request.data.get('locations')
    reponse = requete_openrouteur('cycling-regular', coordonnees)
    return Response(reponse)

@api_view(['POST'])
def itineraire_randonnee(request):
    coordonnees = request.data.get('locations')
    reponse = requete_openrouteur('hiking', coordonnees)
    return Response(reponse)

@api_view(['POST'])
def itineraire_fitness(request):
    coordonnees = request.data.get('locations')
    reponse = requete_openrouteur('foot-walking', coordonnees)
    return Response(reponse)

@api_view(['POST'])
def itineraire_course_groupe(request):
    coordonnees = request.data.get('locations')
    reponse = requete_openrouteur('foot-walking', coordonnees)
    return Response(reponse)

@api_view(['POST'])
def itineraire_marche_recuperation(request):
    coordonnees = request.data.get('locations')
    reponse = requete_openrouteur('foot-walking', coordonnees)
    return Response(reponse)
