from django import forms
from django.contrib.auth.models import User

from .models import UserProfileInfo

# Colocar regra pra cadastrar
# Tipo 0 Doador tipo 1 Empresa
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','password','email')


class UserProfileInfoForm(forms.ModelForm):
    name = forms.CharField(label='Nome',label_suffix='SUFIXO', max_length=255, min_length=3, strip=True, required=True)
    class Meta():
        model = UserProfileInfo
        fields = ('profile_pic', 'user',)
        widgets = {'user': forms.HiddenInput()}
    