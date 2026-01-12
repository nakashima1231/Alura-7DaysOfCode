from django.urls import path
from .views import mostrar_personagem_api

urlpatterns = [
    path("api/", mostrar_personagem_api),
]