from django.db import models
from django.urls import reverse

class Site(models.Model):
    nom = models.CharField(max_length=100)
    url = models.URLField()
    identifiant = models.CharField(max_length=50)
    mot_de_passe = models.CharField(max_length=50)

    def __str__(self):
        return self.nom

    def get_absolute_url(self):
        return reverse('modifier_site', args=[str(self.id)])