from django.contrib import admin
from django.urls import path, include

from products.views import ListProductView, CreateProductView
urlpatterns = [
    path('', ListProductView.as_view()),
    path('create', CreateProductView.as_view()),
]