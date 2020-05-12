from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, FormView, CreateView, DeleteView
from django.urls import reverse, reverse_lazy

from .models import Product, Company
from .forms import ProductForm
from core.models import UserProfileInfo


@login_required
def list_product_view(request):
    products = Product.objects.all()
    return render(request, 'list.html', {'products': products})


class CreateProductView(LoginRequiredMixin, CreateView):
    template_name = "create.html"
    form_class = ProductForm
    success_url = '/products/'

    def post(self, request, *args, **kw):
        company, _ = Company.objects.get_or_create(user=self.request.user.userprofileinfo)
        company.save()
        form = ProductForm(request.POST, files=request.FILES)
        if form.is_valid():            
            prod = form.save(commit=False)
            prod.company = company
            prod.donor = self.request.user.userprofileinfo.donor_set.first()
            prod.save()
            return self.form_valid(form)


class DeleteProductView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('products:list')

class AvaliateProductView(LoginRequiredMixin, TemplateView):
    template_name = "avaliate-product.html"

class ShowCouponView(TemplateView):
    template_name = "coupon.html"