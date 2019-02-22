from django.forms import ModelForm
from .models import Contacto


class ContactoForm(ModelForm):
    class Meta:
        model = Contacto
        fields = ['nombre', 'asunto', 'email', 'texto']


contacto = Contacto.objects.last()
form = ContactoForm(instance=contacto)