from django.shortcuts import HttpResponse

def saludar (request):
  return HttpResponse('Hola mundo')