from django.db import models
from core.models import UserProfileInfo

import uuid

class Donor(models.Model):
    user = models.ForeignKey(UserProfileInfo, on_delete=models.CASCADE)
    created_at = models.DateField('Criado em', auto_now_add=True)


class Company(models.Model):
    user = models.ForeignKey(UserProfileInfo, on_delete=models.CASCADE)
    created_at = models.DateField('Criado em', auto_now_add=True)

class CompanyAssociate(models.Model):
    name = models.CharField('Nome', max_length=255, null=True, blank=True)
    secret = models.UUIDField('Chave_Acesso', primary_key=False, default=uuid.uuid4, editable=False)
    created_at = models.DateField('Criado em', auto_now_add=True)

    def __str__(self):
        return f"{self.name}"


class Coupon(models.Model):
    is_used = models.BooleanField('Cupon Usado', default=False, blank=False, null=False)
    created_at = models.DateField('Criado em', auto_now_add=True)
    donor = models.ForeignKey(UserProfileInfo, on_delete=models.CASCADE, related_name='doador')

class TypeProduct(models.Model):
    ACTIVE_CHOICES = (
        ('active', 'Ativo'),
        ('inactive', 'Inativo'),
    )


    name = models.CharField('Nome', max_length=255, null=False, blank=False)
    active = models.CharField('Ativo', max_length=10, null=False, blank= False, choices=ACTIVE_CHOICES)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    
    def __str__(self):
        return f"{self.name}"

class Product(models.Model):
    STATE_CHOICES = (
        ('waiting','Em Espera'),
        ('approved','Aprovado'),
        ('reproved','Reprovado'),
    )

    name = models.CharField('Nome', max_length=255, null=True, blank=True)
    type = models.ForeignKey(TypeProduct, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.PositiveIntegerField('Quantidade', null=False, blank=False)
    image = models.ImageField('Imagem', upload_to='product_image')
    created_at = models.DateField('Data de criação', auto_now_add=True)
    status = models.CharField('Status', default='waiting', max_length=50, choices=STATE_CHOICES, null=False, blank=False)



    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='empresa')
    donor = models.ForeignKey(Donor, on_delete=models.CASCADE, related_name='doador')

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
    

    def __str__(self):
        return self.name