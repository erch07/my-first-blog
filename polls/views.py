from django.http import HttpResponse


def index(request):
    return HttpResponse("Hola, mundo. Estas en el indice de Encuestas.")
