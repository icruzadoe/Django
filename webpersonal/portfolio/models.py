from django.db import models
# los modelos estan enlazados a la BD
# Create your models here.
class Project(models.Model):
	tittle = models.CharField(max_length=200)  #cadena de caracteres
	description = models.TextField() #campo de caracteres mas grande
	image = models.ImageField() #campo de imagen
	created = models.DateTimeField(auto_now_add=True) #campo de fecha y hora, el atributo es para añadir la hora automaticamente cuando se cree la primera vez (una instancia)
	updated = models.DateTimeField(auto_now=True) # se ejecuta cada vez que se ejecuta una instancia
