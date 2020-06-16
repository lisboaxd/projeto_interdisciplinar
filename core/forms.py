from django import forms
# from django.contrib.auth.models import User

from .models import UserProfileInfo

# Colocar regra pra cadastrar
# Tipo 0 Doador tipo 1 Empresa
class UserForm(forms.ModelForm):
    # password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = UserProfileInfo
        fields = ('username','password','email')


class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('profile_pic', 'email', "first_name", 'username','password','email')
    