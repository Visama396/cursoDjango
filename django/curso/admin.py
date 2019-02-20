from django.contrib import admin
from .models import Cliente,Factura,Grupo,LineaFactura

admin.site.register(Grupo)
admin.site.register(Cliente)
admin.site.register(Factura)
admin.site.register(LineaFactura)