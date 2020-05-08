from django.urls import path
from products.views import list_product_view, CreateProductView

app_name = "products"

urlpatterns = [
    path('', list_product_view, name='list'),
    path('create', CreateProductView.as_view(), name='create'),
]
