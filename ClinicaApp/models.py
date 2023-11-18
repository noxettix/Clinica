from django.db import models
from ClinicaApp.choices import sexos
# Create your models here.

class Paciente(models.Model):
    run =models.CharField(max_length=10,verbose_name='RUN')
    primernombre =models.CharField(max_length=50,verbose_name='Primer nombre')
    primerapellido =models.CharField(max_length=50,verbose_name='Primer apellido')
    segundoapellido = models.CharField(max_length=50,verbose_name='Segundo apellido')
    sexo = models.CharField(max_length=1,choices=sexos,default='m')
    telefono =models.CharField(max_length=20,verbose_name='Telefono')
    mail =models.CharField(max_length=50,verbose_name='Mail')
    direccion =models.CharField(max_length=50,verbose_name='Direccion')
    discapacidad =models.CharField(max_length=50,verbose_name='Discapacidad')
    
    def __str__(self):
        return "{} {} {} {}".format(self.run,self.primernombre,self.primerapellido,self.segundoapellido)

    class Meta:
        db_table = 'paciente'
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'
        ordering = ['run','primernombre','primerapellido','segundoapellido']

