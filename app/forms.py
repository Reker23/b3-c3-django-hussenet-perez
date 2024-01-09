"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _
from django import forms
from .models import Site  # Importez le modèle Site

class SiteForm(forms.ModelForm):
    class Meta:
        model = Site  # Spécifiez le modèle utilisé pour créer le formulaire
        fields = ['nom', 'url', 'identifiant', 'mot_de_passe']  # Liste des champs à inclure dans le formulaire

"""
class BootstrapAuthenticationForm(AuthenticationForm):
    Authentication form which uses boostrap CSS.
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))
"""