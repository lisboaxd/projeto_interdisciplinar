# Generated by Django 3.0.5 on 2020-05-12 23:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20200508_0130'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='company',
        ),
        migrations.AddField(
            model_name='company',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.Product'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='media', verbose_name='Imagem'),
        ),
    ]