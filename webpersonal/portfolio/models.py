from django.db import models
# los modelos estan enlazados a la BD
# Create your models here.
class Project(models.Model):
	tittle = models.CharField(max_length=200, verbose_name="Título")  #cadena de caracteres
	description = models.TextField(verbose_name="Descripción") #campo de caracteres mas grande
	image = models.ImageField(verbose_name="Imagen", upload_to="projects") #campo de imagen, upload_to hace que cada imagen que usban los usuarios creara dentro de la carpeta media una que se llame project y ahi guardara las imagenes
	link = models.URLField(verbose_name="Dirección web", null=True, blank=True)
	created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación") #campo de fecha y hora, el atributo es para añadir la hora automaticamente cuando se cree la primera vez (una instancia)
	updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición") # se ejecuta cada vez que se ejecuta una instancia

	class Meta:
		verbose_name= "proyecto"
		verbose_name_plural = "proyectos"
		ordering = ["-created"]

	def __str__(self):
		return self.tittle