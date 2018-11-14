from django.db import models


class Formulario(models.Model):
    CorreoElectronico=models.CharField(max_length=100)
    Run=models.CharField(max_length=10)
    Nombre=models.CharField(max_length=50)
    FechaNacimiento=models.DateField()
    Telefono=models.IntegerField()
    region=models.CharField(max_length=50)
    Comuna=models.CharField(max_length=50)
    TipoCasa=models.CharField(max_length=50)
    
    def __str__(self):
        return self.Run

class rescatados(models.Model):
    Nombreresc=models.CharField(max_length=100)
    RazaPredom=models.CharField(max_length=100)
    Descripcion=models.TextField(max_length=100)
    Estado=models.CharField(max_length=100)
    image=models.FileField(upload_to='albums',default='SOME STRING')
    
    
    def __str__(self):
        return self.Nombreresc



# Create your models here.
