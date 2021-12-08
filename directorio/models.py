from django.db import models

SECCIONTYPE = [('Administracion','Administracion'), ('Informática','Informática'), ('Pedagogia','Pedagogia'), ('Fomento a la Salud','Fomento a la Salud'), ('Alimentación','Alimentación')]

class Encargado(models.Model):
    nombre = models.CharField(max_length=50, verbose_name='Nombre completo')
    type = models.CharField(choices=SECCIONTYPE, verbose_name='Area', max_length=50)
    foto = models.ImageField(verbose_name= 'Foto', null=True, upload_to='imgProducts')
    

    def __str__(self):
        return "Encargado: {0} {1}".format(self.nombre, self.type, self.foto)

        class Meta:
            verbose_name = "Encargado"
            verbose_name_plural = "Encargados"
            
