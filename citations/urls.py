from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_citations, name='liste_citations'),
    path('ajouter/', views.ajouter_citation, name='ajouter_citation'),
]
