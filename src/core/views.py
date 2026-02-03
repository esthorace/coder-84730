from django.http import HttpResponse
from django.shortcuts import render


def saludar(request):
    return HttpResponse("Hola desde Django!")


def saludar_con_etiqueta(request):
    return HttpResponse("<h1>Uso de etiquetas HTML</h1>")


def index(request):
    return render(request, "core/index.html", {"titulo": "Python - Django"})


def tirar_dado(request):
    from datetime import datetime
    from random import randint

    tiro_de_dado = randint(1, 6)
    if tiro_de_dado == 6:
        mensaje = f"Has tirado el 🎲 y has obtenido {tiro_de_dado}, 🥂 GANASTE!"
    else:
        mensaje = f"Has tirado el 🎲 y has obtenido {tiro_de_dado}, 🙁 PERDISTE!"
    datos = {
        "titulo": "Tiro de Dados",
        "mensaje": mensaje,
        "fecha": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
    }
    return render(request, "core/tirar_dado.html", datos)


def notas(request):
    mis_notas = [10, 7, 4, 6, 8, 8]
    return render(request, "core/notas.html", context={"notas": mis_notas})
