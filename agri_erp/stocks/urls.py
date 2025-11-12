from django.urls import path
from . import views

app_name = "stocks"

urlpatterns = [
    path("", views.product_list, name="product_list"),
    path("commande/nouvelle/", views.order_create, name="order_create"),
    path("commande/<int:pk>/", views.order_detail, name="order_detail"),
]
