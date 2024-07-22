from django import forms


class FormularioContacto(forms.Form):
    nombre=forms.CharField(label='Nombre', max_length=25, required=True) 
    email=forms.EmailField(label='Email', required=True)
    contenido=forms.CharField(label='Contenido', widget=(forms.Textarea) ,required=True)

