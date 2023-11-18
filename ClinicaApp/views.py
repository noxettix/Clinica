from django.shortcuts import render,redirect, get_object_or_404 
from ClinicaApp.forms import PacienteForm
from ClinicaApp.models import Paciente
# Create your views here.

def inicio(request):
    pacientes = Paciente.objects.all()
    data ={
        'pacientes':pacientes,
    }
    return render(request, 'iniciodepagina/pacientes.html', data)

def todos_pacientes(request):
    pacientes = Paciente.objects.all()
    data ={
        'pacientes':pacientes,
    }
    return render(request, 'iniciodepagina/pacientes.html', data)

def ingresar_paciente(request):
    if request.method =='POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='pacientes')
    else:
        form = PacienteForm()
    
    return render(request, 'iniciodepagina/ingresopaciente.html', {'form': form})

def cargar_editar_paciente(request, id):
    Pacientes = get_object_or_404(Paciente, id)
    form = PacienteForm(instance=Paciente)

    return render(request, 'iniciodepagina/pacienteEdit.html', {'form': form,'Pacientes':Pacientes})

def modificar_paciente(request, id):
    Pacientes = get_object_or_404(Pacientes,id=id)

    if request.method == 'POST':
        form = PacienteForm(request.POST, instance=Paciente)
        if form.is_valid():
            form.save()
            return redirect('/pacientes/')
    else:
        form = PacienteForm(instance=Paciente)
    return render(request, 'iniciodepagina/paciente.html', {'form':form})

def eliminar_paciente(request, id):
    paciente = get_object_or_404(Paciente,id=id)

    if request.method == 'POST':
        paciente.delete()
        #return redirect ('/pacientes')
    return render(request, 'iniciodepagina/eliminarpaciente.html', {'pacientes': Paciente})
    