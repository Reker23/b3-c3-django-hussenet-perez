"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render,get_object_or_404, redirect
from django.http import HttpRequest
from .models import Site  # Importez le modèle Site depuis votre application
from .forms import SiteForm  # Importez le formulaire SiteForm
from django.contrib import messages

def site_liste(request):
    sites = Site.objects.all()  # Récupérer tous les objets Site depuis la base de données
    return render(request, 'app/index.html', {'title': 'Liste des Sites','sites': sites,})

def ajouter_site(request):
    if request.method == 'POST':
        form = SiteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('site_liste')  # Redirection vers la vue 'site_liste' après avoir enregistré le site
    else:
        form = SiteForm()

    return render(request, 'app/ajout_site.html', {'form': form})

def supprimer_site(request, site_id):
    site = get_object_or_404(Site, pk=site_id)
    
    if request.method == 'POST':
        site.delete()  # Supprimez le site de la base de données
        print(f"Le site avec l'ID {site_id} a été supprimé.")  # Ajout d'un message de débogage
        return redirect('app/index.html')  # Redirigez l'utilisateur vers une autre page après la suppression
    
    return render(request, 'app/supprimer_site.html', {'site': site})


def modifier_site(request, site_id):
    site = get_object_or_404(Site, pk=site_id)
    
    if request.method == 'POST':
        form = SiteForm(request.POST, instance=site)
        if form.is_valid():
            form.save()
            return redirect('app/index.html')
    else:
        form = SiteForm(instance=site)
    
    return render(request, 'app/modifier_site.html', {'form': form, 'site': site})