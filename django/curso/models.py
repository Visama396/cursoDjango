from django.db import models


class Cliente(models.Model):
    nombre = models.CharField(max_length=30)
    cif = models.CharField(max_length=9, primary_key=True)
    tlf = models.IntegerField()
    fax = models.IntegerField()
    url = models.URLField(max_length=40)
    email = models.EmailField(max_length=35)
    activo = models.BooleanField()
    fecha_alta = models.DateField()
    numero_trabajadores = models.IntegerField()

    def __str__(self):
        return self.nombre + " " + self.cif;
