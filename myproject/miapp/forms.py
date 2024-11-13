from django import forms
from .models import RespuestaFormulario


class ContactForm(forms.Form):
    name = forms.CharField(label='Nombre', max_length=100)
    email = forms.EmailField(label='Email')
    message = forms.CharField(widget=forms.Textarea, label='Mensaje')

class RespuestaFormularioForm(forms.ModelForm):
    class Meta:
        model = RespuestaFormulario
        fields = ['nombre', 'correo', 'mensaje']
