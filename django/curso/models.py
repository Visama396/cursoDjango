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
    fecha_alta = models.DateField(default="0000-00-00")

    def __str__(self):
        return self.nombre


class Factura(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    numero = models.IntegerField()
    total = models.DecimalField(max_digits=20, decimal_places=2)
    serie = models.CharField(max_length=15)

    def __str__(self):
        return self.serie

    def save(self, *args, **kwargs):
        self.total = sum(l.total for l in self.lineas.all())

        if not self.pk:
            proximo = 1
            ultima = Factura.objects.filter(serie=self.serie).order_by("-numero").first()
            if ultima:
                proximo = ultima.numero + 1
            self.numero = proximo

        super().save(*args, **kwargs)


class LineaFactura(models.Model):
    factura = models.ForeignKey(Factura, on_delete=models.CASCADE, related_name="lineas")
    articulo = models.CharField(max_length=125, default="")
    cantidad = models.IntegerField(default=1)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.articulo

    def save(self, *args, **kwargs):
        self.total = self.cantidad * self.precio
        super().save(*args, **kwargs)


class Contacto(models.Model):
    nombre = models.CharField(max_length=120, default="")
    asunto = models.CharField(max_length=255, default="")
    email = models.EmailField(max_length=255, default="")
    texto = models.CharField(max_length=255, default="")

    def __str__(self):
        return "Mr./Mrs. {} - {}".format(self.nombre, self.asunto)

