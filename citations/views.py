from django.shortcuts import render, redirect
from .models import Citation
import random

def liste_citations(request):
    # Récupère toutes les citations de la base de données
    citations = Citation.objects.all().order_by('-date_creation')
    return render(request, 'citations/liste.html', {'citations': citations})

def ajouter_citation(request):
    if request.method == "POST":
        auteur = request.POST.get('auteur')
        texte = request.POST.get('texte')
        
        # Génération d'une couleur aléatoire pour le fond
        # On génère des composants RGB aléatoires
        r = random.randint(100, 255)
        g = random.randint(100, 255)
        b = random.randint(100, 255)
        couleur = f"#{r:02x}{g:02x}{b:02x}"

        # Création et sauvegarde de la citation
        Citation.objects.create(
            auteur=auteur,
            texte=texte,
            couleur_fond=couleur
        )
        return redirect('liste_citations')
    
    # Si la requête est GET (on affiche juste le formulaire)
    return render(request, 'citations/ajouter.html')