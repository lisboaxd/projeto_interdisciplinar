from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView
from .models import Product

def ListProductView(request):
    products = Product.objects.all()
    return render(request, 'list.html', {'products': products})


class CreateProductView(LoginRequiredMixin, TemplateView):
    template_name = "create.html"