from django.contrib import admin
from .models import Cliente,Factura,Grupo,LineaFactura

class ClienteAdmin(admin.ModelAdmin):
    search_fields = ["nombre", "nif"]
    list_display = ["nombre", "nif", "activo"]
    list_filter = ["activo", "grupos"]
    date_hierarchy = "fecha_alta"
    filter_horizontal = ["grupos"]


class LineaFacturaInline(admin.TabularInline):
    model = LineaFactura
    readonly_fields = ["total"]

class FacturaAdmin(admin.ModelAdmin):
    search_fields = ["numero", "serie"]
    list_display = ["cliente", "numero", "serie"]
    list_filter = ["cliente"]
    inlines = [LineaFacturaInline]
    readonly_fields = ["total"]
    fieldsets = (
        ("Factura", {
            "fields": (("cliente", "total"),
                       ("numero"), "serie")
        }),
    )

    def save_related(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)
        form.instance.save()


admin.site.register(Grupo)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Factura, FacturaAdmin)
admin.site.register(LineaFactura)