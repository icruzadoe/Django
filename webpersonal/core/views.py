from django.shortcuts import render,HttpResponse

# Create your views here.
# una vista hace referencia a la logica que se ejecuta cuando se hace 0
# una peticion a nuestra web

def home(request):
	return render(request, "core/home.html")

def about(request):
	return render(request, "core/about.html")

def portafolio(request):
	return render(request, "core/portafolio.html")

def contact(request):
	return render(request, "core/contact.html")