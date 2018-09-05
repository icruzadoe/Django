from django.shortcuts import render
from .models import Project

# Create your views here.
def portafolio(request):
	#recuperar la lista de proyectos
	projects = Project.objects.all()
	#para pasar datos al template pasamos en el render como 3er parametro un diccionario
	return render(request, "portfolio/portafolio.html",{'projects':projects})