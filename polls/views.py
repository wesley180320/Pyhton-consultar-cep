from urllib import request

from django.http import HttpResponse
from django.shortcuts import render
import requests

from . import models


def index(request):


    if request.method == "POST":
        cep = request.POST.get('cep', None)
        requisicao = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
        dados2 = requisicao.json()

        print(dados2['cep'])

        endereco = models.dados()
        endereco.localidade = dados2['localidade']
        endereco.rua = dados2['logradouro']
        endereco.bairro = dados2['bairro']
        endereco.save()

    return render(request, 'polls/index.html')

