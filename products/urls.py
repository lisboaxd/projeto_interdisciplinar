from django.urls import path
from products.views import (
    list_product_view, CreateProductView,
    list_coupon_view, avaliate,
    DeleteProductView, UpdateProductView,
    aprove_product
    )


app_name = "products"

urlpatterns = [
    path('', list_product_view, name='list'),
    path('create', CreateProductView.as_view(), name='create'),
    path('edit/<int:pk>', UpdateProductView.as_view(), name='edit'),
    path('delete/<int:pk>', DeleteProductView.as_view(), name='delete'),
    path('avaliate', avaliate, name='avaliate'),
    path('coupon', list_coupon_view, name='coupon'),
    path('aprove/<int:pk>', aprove_product, name='aprove'),
]
