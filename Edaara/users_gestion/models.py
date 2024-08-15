from django.db import models

# Create your models here.

class User(models.Model):
    nom = models.CharField( max_length=50)
    prenom = models.CharField(max_length=100)
    date_naissance = models.DateField()
    sexe = models.CharField(max_length=20, sexe_choices=[('feminin', 'Feminin'), ('masculin', 'Masculin')], default='masculin')
    email = models.EmailField(unique=True)
    statut = models.CharField(max_length=20, statut_choices=[('apprenant', 'Apprenant'), ('formateur', 'Formateur')])
    mots_de_passe = models.CharField(max_length=100)