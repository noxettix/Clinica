from django import forms
from ClinicaApp.models import Paciente
from ClinicaApp.choices import sexos

class PacienteForm(forms.ModelForm):
    run =forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: 12345678-9', 'maxlength': '10'}))
    primernombre =forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ingrese el nombre'}))
    primerapellido =forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ingrese el primer apellido'}))
    segundoapellido = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ingrese el segundo apellido'}))
    sexo = forms.CharField(widget=forms.Select(choices=sexos, attrs={'class': 'form-select'}))
    telefono =forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: 123456789'}))
    mail =forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ingrese el mail'}))
    direccion =forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ingrese la direccion'}))
    discapacidad =forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ingrese la discapacidad'}))

    class Meta:
            model = Paciente
            fields = '__all__'

#class especialista(forms.ModelForm):
#    run =forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: 12345678-9'}))
#    primernombre =forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ingrese el nombre'}))
#    segundonombre = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ingrese el segundo nombre'}))
#    primerapellido =forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ingrese el primer apellido'}))
#    segundoapellido = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ingrese el segundo apellido'}))
#    sexo = forms.CharField(widget=forms.Select(choices=sexos, attrs={'class': 'form-select'}))
#    telefono =forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: 123456789'}))
#    mail =forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ingrese el mail'}))
 #   direccion =forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ingrese la direccion'}))


 #   class Meta:
 #       model = especialista
 #       fields = '__all__'