from django.urls import path
from products.views import (
    list_product_view, CreateProductView,
    list_coupon_view, AvaliateProductView,
    DeleteProductView
    )


app_name = "products"

urlpatterns = [
    path('', list_product_view, name='list'),
    path('create', CreateProductView.as_view(), name='create'),
    path('delete/<int:pk>', DeleteProductView.as_view(), name='delete'),
    path('avaliate', AvaliateProductView.as_view(), name='avaliate'),
    path('coupon', list_coupon_view, name='coupon')
]
