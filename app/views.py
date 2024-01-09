"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from .models import Site  # Importez le modèle Site depuis votre application
from .forms import SiteForm  # Importez le formulaire SiteForm
from django.contrib import messages

def site_liste(request):
    sites = Site.objects.all()  # Récupérer tous les objets Site depuis la base de données
    return render(request, 'app/index.html', {'title': 'Liste des Sites','sites': sites,})

def ajouter_site(request):
    if request.method == 'POST':
        form = SiteForm(request.POST)  # Créez une instance du formulaire avec les données POST
        if form.is_valid(): # Si le formulaire est validé, on l'enregistre dans la BDD
            form.save()  # Enregistrez les données dans la base de données si le formulaire est valide
            messages.success(request, 'Le site a été ajouté avec succès !')  # Ajoutez un message de succès
    else:
        form = SiteForm()  # Créez une instance vide du formulaire pour affichage

    return render(request, 'app/ajout_site.html', {'form': form})


def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )
