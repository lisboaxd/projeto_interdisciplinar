from django.forms import ModelForm
from .models import Product, Donor, Company

class ProductForm(ModelForm):

    class Meta:
        model = Product
        fields = ("name", "type", "quantity", "image")
        labels = {
            'name': 'Nome',
            'type': 'Tipo',
            'quantity': 'Quantidade',
            'image': 'Imagem',
        }


class DonorForm(ModelForm):

    class Meta:
        model = Donor
        fields = ('user',)

class CompanyForm(ModelForm):

    class Meta:
        model = Company
        fields = ('user',)