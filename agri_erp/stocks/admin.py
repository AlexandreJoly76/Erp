from django.contrib import admin
from .models import Client, Commande, LigneCommande, Produit


@admin.register(Produit)
class ProduitAdmin(admin.ModelAdmin):
    list_display = ("ref", "nom", "prix", "quantite", "valeur_stock", "created_at")
    search_fields = ("ref", "nom")
    list_filter = ("created_at",)
    ordering = ("ref",)


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("nom", "email", "type_client", "created_at")
    search_fields = ("nom", "email")
    list_filter = ("type_client", "created_at")


class LigneCommandeInline(admin.TabularInline):
    model = LigneCommande
    extra = 1
    autocomplete_fields = ("produit",)


@admin.register(Commande)
class CommandeAdmin(admin.ModelAdmin):
    list_display = ("id", "client", "date", "status", "total_ht", "total_ttc")
    search_fields = ("client__nom", "id")
    list_filter = ("status", "date")
    ordering = ("-date",)
    inlines = [LigneCommandeInline]
    autocomplete_fields = ("client",)
