from django.db import models
from django.contrib.auth.models import User


class Persona(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True)
    nombrePersona=models.CharField(max_length=30)
    apellidoPersona=models.CharField(max_length=30)
    fechaNacimiento=models.DateField()
    numeroFono=models.CharField(max_length=10,null=True,blank=True)
    regionPersona=models.CharField(max_length=50)
    ciudadPersona=models.CharField(max_length=50)
    viviendaPersona=models.CharField(max_length=50)
    tipoPersona=models.CharField(max_length=50, default="Usuario")


def __str__(self):
 return self.nombrePersona+ " "+self.apellidoPersona


class Mascota(models.Model):
    codigoMascota=models.AutoField(primary_key=True)
    imagen=models.ImageField(upload_to='./Sistema/static/media/img_perros')
    nombreMascota=models.CharField(max_length=20)
    razaMascota=models.CharField(max_length=50)
    descripcionMascotra=models.TextField(null=True, blank=True)
    estadoMascota=models.CharField(max_length=50,default="rescatado")

def __str__(self):
 return self.nombreMascota
