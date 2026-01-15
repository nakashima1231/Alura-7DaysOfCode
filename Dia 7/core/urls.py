from django.urls import path
from . import views

urlpatterns = [
    path("personagens/", views.mostrar_personagem_api, name = "personagens"),
]