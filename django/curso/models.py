from django.db import models


class Grupo(models.Model):
    nombre = models.CharField(max_length=155)

    def __str__(self):
        return self.nombre


class Cliente(models.Model):
    nombre = models.CharField(max_length=255)
    nif = models.CharField(max_length=15, default="")
    direccion = models.CharField(max_length=125, default="")
    activo = models.BooleanField(default=True)
    grupos = models.ManyToManyField(Grupo)

    def __str__(self):
        return self.nombre


class Factura(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    numero = models.IntegerField()
    total = models.DecimalField(max_digits=20, decimal_places=2)
    serie = models.CharField(max_length=15)

    def __str__(self):
        return self.serie


class LineaFactura(models.Model):
    factura = models.ForeignKey(Factura, on_delete=models.CASCADE)
    descripcion = models.TextField()
    unidades = models.IntegerField(default=1)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.descripcion

