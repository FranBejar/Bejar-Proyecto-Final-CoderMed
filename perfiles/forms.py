from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='DNI', help_text='(Solo numeros, sin puntos)', max_length=10)
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir Contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['last_name', 'first_name', 'username', 'email', 'password1', 'password2']
        
    def __init__(self, *args , **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)

        self.fields['username'].label='DNI'
        self.fields['username'].help_text='(Solo numeros, sin puntos)'

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label='DNI', max_length=10)

    def __init__(self, *args, **kwargs):
        super(CustomAuthenticationForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = 'DNI'