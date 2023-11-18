from django.contrib import admin

# Register your models here.
from ClinicaApp.models import Paciente

class PacienteAdmin(admin.ModelAdmin):
    list_display = ['run','primernombre','primerapellido','segundoapellido','telefono','mail','direccion','discapacidad']

admin.site.register(Paciente,PacienteAdmin)