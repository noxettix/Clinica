from django.contrib import admin
from django.urls import path ,include
from ClinicaApp import views as vistas
urlpatterns = [
    path('admin/', admin.site.urls),
    path('' ,vistas.inicio,name='inicio'),
    path('ingresarPaciente/' ,vistas.ingresar_paciente,name='ingresarPaciente'),
    path('pacientes/',vistas.todos_pacientes,name='pacientes'),
    path('pacienteEdit/<int:id>/',vistas.cargar_editar_paciente,name='editarPaciente'),
    path('pacienteEditado/<int:id>/',vistas.modificar_paciente,name='pacienteEditado'),
    path('eliminarPaciente/<int:id>/',vistas.eliminar_paciente,name='eliminarPaciente'),
]
