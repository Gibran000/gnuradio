from django.shortcuts import render
from django.http import HttpResponse


def index(request):
	return render(request, 'polls/index.html', {})

def services(request):
	return render(request, 'polls/services.html', {})

def about(request):
	return render(request, 'polls/about.html', {})

def bloque(request):
	return render(request, 'polls/bloque.html', {})

def pruebas(request):
	return render(request, 'polls/pruebas.html', {})

def instalacion(request):
	return render(request, 'polls/instalacion.html', {})

# def someview(request):
#     if request.method == "POST":
#         country_name = request.POST['country']

#     somemodel.objectname = countryname
#     somemodel.save()