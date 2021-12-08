from django.db import models

POLITICATYPE = [('Valores','Valores'), ('Misión','Misión'), ('Visión','Visión'), ('Objetivo','Objetivo')]


class Contenido(models.Model):
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    detalles = models.CharField(max_length=500, verbose_name='Detalles')
    type = models.CharField(choices=POLITICATYPE, verbose_name='Tipo de Registro', max_length=50)
    foto = models.ImageField(verbose_name= 'Foto', null=True, upload_to='imgProducts')
    

    def __str__(self):
        return "{0} {1}".format(self.nombre, self.detalles, self.type, self.foto)

        class Meta:
            verbose_name = "Contenido"
            verbose_name_plural = "Contenidos"
            
