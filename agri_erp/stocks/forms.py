from django import forms
from django.forms import inlineformset_factory
from .models import Commande, LigneCommande

class CommandeForm(forms.ModelForm):
    class Meta:
        model = Commande
        fields = ["client", "status","tva"]

LigneCommandeFormSet = inlineformset_factory(
    parent_model=Commande,
    model=LigneCommande,
    fields=["produit", "quantite", "prix_unitaire"],
    extra=3,
    can_delete=False,
)
