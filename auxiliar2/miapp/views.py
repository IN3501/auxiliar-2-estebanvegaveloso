from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'miapp/index.html')
def equipo(request):
	return render(request, 'miapp/equipo.html')
def libre(request):
	return render(request, 'miapp/libre.html')


	