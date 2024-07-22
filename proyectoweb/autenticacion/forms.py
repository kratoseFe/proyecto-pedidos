from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserCreationformWhithEmail(UserCreationForm):
    email= forms.EmailField(required=True,
        help_text="Requerido. 254 carácteres como maximo y debe ser un email válido",
        widget= forms.EmailInput(attrs={'class': 'form-contol mb-2', 'placeholder': 'Dirección de correo'})
        )
    
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


    def save(self, commit=True):
        user = super(UserCreationformWhithEmail, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            return user