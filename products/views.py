from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView

from .models import Product

@login_required
def list_product_view(request):
    products = Product.objects.all()
    return render(request, 'list.html', {'products': products})


class CreateProductView(LoginRequiredMixin, TemplateView):
    template_name = "create.html"