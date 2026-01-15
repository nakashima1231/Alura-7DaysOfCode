from django.shortcuts import render
import requests
from django.core.paginator import Paginator
from googletrans import Translator

async def mostrar_personagem_api(request):
    api_url = "https://last-airbender-api.fly.dev/api/v1/characters"
    personagens = requests.get(api_url).json()

    paginator = Paginator(personagens, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    tradutor = Translator()

    for p in page_obj:
        nome = p.get("name", "")
        afiliacao = p.get("affiliation", "")

        if nome:
            p["name_traduzido"] = (await tradutor.translate(nome, dest="pt")).text
        else:
            p["name_traduzido"] = ""

        if afiliacao:
            p["afiliacao_traduzida"] = (await tradutor.translate(afiliacao, dest="pt")).text
        else:
            p["afiliacao_traduzida"] = "Não informado"

    return render(request, "personagens.html", {
        "page_obj": page_obj
    })
