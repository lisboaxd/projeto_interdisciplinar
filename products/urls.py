from django.urls import path
from products.views import ListProductView, CreateProductView

app_name = "products"

urlpatterns = [
    path('', ListProductView, name='list'),
    path('create', CreateProductView.as_view(), name='create'),
]
