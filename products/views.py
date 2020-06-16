from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, ListView, FormView, CreateView, DeleteView, edit
from django.urls import reverse, reverse_lazy
from rest_framework.viewsets import ModelViewSet
from rest_framework.serializers import ModelSerializer

from .models import Product, Company, Coupon, Donor, CompanyAssociate
from .forms import ProductForm
from core.models import UserProfileInfo


@login_required
def list_product_view(request):
    user = ''
    products = ''
    donor = True
    try:
        user = request.user.donor
        products = Product.objects.filter(donor=user)
    except Exception as e:
        user = request.user.company
        products = Product.objects.filter(company=user)
        donor = False
    
    return render(request, 'list.html', {'products': products, 'donor': donor})

@login_required
def list_coupon_view(request):
    coupons = Coupon.objects.filter(donor=request.user)
    return render(request, 'coupon.html', {'coupons': coupons})


@login_required
def aprove_product(request, pk):
    company = request.user.company
    product = get_object_or_404(Product, pk=pk, status='waiting')
    if product:
        product.company = company
        product.status = 'approved'
        product.save()
        products = Product.objects.filter(company=company)
        coupon = Coupon(donor=product.donor.user)
        coupon.save()
        return render(request, 'avaliate-product.html', {
            'products': products,
            'coupon': coupon
            })
    else:
        return redirect('/products/')

@login_required
def avaliate(request):
    user = request.user.company
    products = Product.objects.filter(status='waiting')
    donor = False
    return render(request, 'list.html', {'products': products, 'donor': donor})


class CreateProductView(LoginRequiredMixin, CreateView):
    template_name = "create.html"
    form_class = ProductForm
    success_url = '/products/'

    def post(self, request, *args, **kw):
        form = self.form_class(request.POST, files=request.FILES)
        if form.is_valid():
            # TODO: validar se usuário é do tipo donor, se não for, retornar mensagem de erro
            prod = form.save(commit=False)
            prod.donor = self.request.user.donor
            prod.save()
            return self.form_valid(form)

class UpdateProductView(LoginRequiredMixin, edit.UpdateView):
    template_name = "create.html"
    model = Product
    form_class = ProductForm
    success_url = '/products/'
    # fields = ['name',]



class DeleteProductView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('products:list')

class AvaliateProductView(LoginRequiredMixin, TemplateView):
    template_name = "avaliate-product.html"

class ShowCouponView(LoginRequiredMixin, TemplateView):
    template_name = "coupon.html"


def list_donors(request):
    donors = Donor.objects.all()
    return render(request, 'donors/list.html',{'donors':donors})


class UserSerializer(ModelSerializer):
    
    class Meta:
        model = UserProfileInfo
        fields = ['first_name', 'id']
        
class DonorSerializer(ModelSerializer):
    
    class Meta:
        model = Donor
        fields = ['user', 'id']

class CouponSerializer(ModelSerializer):
    donor = UserSerializer(many=False, read_only=True)
    class Meta:
        model = Coupon
        fields = '__all__'


class CouponViewSet(ModelViewSet):
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer

class DonorsViewSet(ModelViewSet):
    queryset = Donor.objects.all()
    serializer_class = DonorSerializer