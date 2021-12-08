from django.db import models


# Create your models here.
class Compra (models.Model):
    nombre = models.CharField(verbose_name='Nombre del producto', max_length=100, unique=True)
    descripcion = models.TextField(verbose_name='Descripción del producto', max_length=1000)
    
    def __str__(self):
        return "{0} {1}".format(self.nombre, self.descripcion)


    class Meta:
        verbose_name= 'Compra'
        verbose_name_plural= 'Compras'

AREATYPE = [('Administracion','Administracion'), ('Pedagogia','Pedagogia'), ('Fomento a la Salud','Fomento a la Salud'), ('Alimentación','Alimentación')]

class Almacen (models.Model):
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE, verbose_name='Compra')
    ingreso = models.DateTimeField(verbose_name='Fecha y hora de ingreso')
    area = models.CharField(choices=AREATYPE, verbose_name='Area', max_length=50)

    def __str__(self):
        return 'Compra {0}, se ingresó el {1}'.format(self.compra, self.ingreso, self.area)

    class Meta:
        verbose_name = 'Almacen'
        verbose_name_plural = 'Almacen'