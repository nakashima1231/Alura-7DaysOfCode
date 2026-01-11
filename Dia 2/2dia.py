import json
import requests
import asyncio
from googletrans import Translator

async def traduzir():
    api_url = f'https://last-airbender-api.fly.dev/api/v1/characters'
    personagens = (requests.get(api_url)).json()

    tradutor = Translator()
    for p in personagens:
        nome = p.get("name", "")
        afiliacao = p.get("affiliation", "")

        af = await tradutor.translate(afiliacao, dest="pt")
        p["affiliacao_traduzida"] = af.text
    
        na = await tradutor.translate(nome, dest="pt")
        p["name_traduzido"] = na.text



    print(personagens)

asyncio.run(traduzir())