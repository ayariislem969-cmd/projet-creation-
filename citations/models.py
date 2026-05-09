from django.db import models

class Citation(models.Model):
    auteur = models.CharField(max_length=100)
    texte = models.TextField()
    # Nous allons stocker la couleur en format hexadécimal (ex: #FF5733)
    couleur_fond = models.CharField(max_length=7, default='#FFFFFF')
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.auteur} : {self.texte[:30]}..."