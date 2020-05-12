from django.forms import ModelForm
from .models import Product

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