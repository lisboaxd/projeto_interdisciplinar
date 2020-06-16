from django.db import models
from django.contrib.auth.models import AbstractUser

class UserProfileInfo(AbstractUser):
    # user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)
    created_at = models.DateField('Criado em', auto_now_add=True)

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfis'

    def __str__(self):
        return self.username