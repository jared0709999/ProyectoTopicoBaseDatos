from django.db import models

SECCIONTYPE = [('Administracion','Administracion'), ('Pedagogia','Pedagogia'), ('Fomento a la Salud','Fomento a la Salud'), ('Alimentación','Alimentación')]

class Foto(models.Model):
    fecha = models.DateField()
    type = models.CharField(choices=SECCIONTYPE, verbose_name='Tipo de Registro', max_length=50)
    detalles = models.CharField(max_length=500, verbose_name='Detalles')
    foto = models.ImageField(verbose_name= 'Foto', null=True, upload_to='imgProducts')
    

    def __str__(self):
        return "Foto: {0} {1}".format(self.fecha, self.type, self.detalles, self.foto)

        class Meta:
            verbose_name = "Foto"
            verbose_name_plural = "Foto"
            
