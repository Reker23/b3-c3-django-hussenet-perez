"""
Definition of urls for passwordManager.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views


urlpatterns = [
    path('', views.site_liste, name='site_liste'),
    path('supprimer_site/<int:site_id>/', views.supprimer_site, name='supprimer_site'),
    #une pour modifier
    path('ajout/', views.ajouter_site, name='ajout'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
]
