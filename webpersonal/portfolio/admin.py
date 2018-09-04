from django.contrib import admin
from .models import Project #con el . adelante de models sabemos que estamos haciendo referencia al mismo directorio en este caso portfolio

# Register your models here.

#Modifica el panel del administrador para que muestre la fecha de creacion y la fecha de edicion
class ProjectAdmin(admin.ModelAdmin):
	readonly_fields = ('created', 'updated')

#se pasa como parametro la configuracion extendida para que se muestre
admin.site.register(Project, ProjectAdmin)