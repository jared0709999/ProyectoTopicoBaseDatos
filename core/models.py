from django.db import models

class Area (models.Model):
    nombre = models.CharField(verbose_name='Sala de Atención', max_length=100)
    rango = models.CharField(verbose_name= 'Rango de edad', max_length=100)
    foto = models.ImageField(verbose_name= 'Foto', null=True, upload_to='imgProducts')

    def __str__(self):
        return "{0} {1}".format(self.nombre, self.rango, self.foto)

    class Meta:
        verbose_name="Sala"
        verbose_name_plural="Salas"

   


REGISTRYTYPE = [('Empleado','Empleado'), ('Niño','Niño'), ('Padre','Padre')]
GENDERTYPE = [('Hombre','Hombre'), ('Mujer','Mujer')]
SECCIONTYPE = [('Administracion','Administracion'), ('Pedagogia','Pedagogia'), ('Fomento a la Salud','Fomento a la Salud'), ('Alimentación','Alimentación')]


class Registro(models.Model):
    nombre = models.CharField(max_length=50, verbose_name='Nombre (s)')
    apellido = models.CharField(max_length=50, verbose_name='Apellidos')
    seccion = models.CharField(choices=SECCIONTYPE, verbose_name='Area', max_length=50)
    area = models.ForeignKey(Area, on_delete=models.CASCADE, verbose_name='Sala de atención')
    ingreso = models.DateField()
    nacimiento = models.DateField()
    curp = models.CharField(max_length=50, verbose_name='CURP')
    nss = models.CharField(max_length=50, verbose_name='NSS')
    telefono = models.CharField(max_length=50, verbose_name='Número telefónico')
    direccion = models.CharField(max_length=500, verbose_name='dirección')
    type = models.CharField(choices=REGISTRYTYPE, verbose_name='Tipo de Registro', max_length=50)
    gender = models.CharField(choices=GENDERTYPE, verbose_name='Sexo', max_length=50)
    foto = models.ImageField(verbose_name= 'Foto', null=True, upload_to='imgProducts')
    

    def __str__(self):
        return "Registro: {0} {1}".format(self.nombre, self.apellido, self.seccion, self.area, self.ingreso, self.nacimiento, self.curp, self.nss, self.telefono, self.direccion, self.type, self.gender, self.foto)

        class Meta:
            verbose_name = "Registro"
            verbose_name_plural = "Registros"
            
