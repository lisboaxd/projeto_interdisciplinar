from django.db import models

# Create your models here.
class TypeProduct(models.Model):
    name = models.CharField('Nome', max_length=255, null=True, blank=True)

class Product(models.Model):
    name = models.CharField('Nome', max_length=255, null=True, blank=True)
    type = models.ForeignKey(TypeProduct, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.PositiveIntegerField('Quantidade', null=False, blank=False)
    image = models.ImageField('Imagem', upload_to='product_image')