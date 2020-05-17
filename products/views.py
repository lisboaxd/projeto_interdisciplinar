from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, FormView, CreateView, DeleteView
from django.urls import reverse, reverse_lazy

from .models import Product, Company, Coupon
from .forms import ProductForm
from core.models import UserProfileInfo


@login_required
def list_product_view(request):
    products = Product.objects.all()
    return render(request, 'list.html', {'products': products})

@login_required
def list_coupon_view(request):
    coupons = Coupon.objects.all()
    return render(request, 'coupon.html', {'coupons': coupons})


class CreateProductView(LoginRequiredMixin, CreateView):
    template_name = "create.html"
    form_class = ProductForm
    success_url = '/products/'

    def post(self, request, *args, **kw):
        form = self.form_class(request.POST, files=request.FILES)
        if form.is_valid():
            # TODO: validar se usuário é do tipo donor, se não for, retornar mensagem de erro
            prod = form.save(commit=False)
            prod.donor = self.request.user.userprofileinfo.donor
            prod.save()
            return self.form_valid(form)


class DeleteProductView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('products:list')

class AvaliateProductView(LoginRequiredMixin, TemplateView):
    template_name = "avaliate-product.html"

class ShowCouponView(LoginRequiredMixin, TemplateView):
    template_name = "coupon.html"