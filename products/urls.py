from django.contrib import admin
from django.urls import path, include

from products.views import IndexProductView
urlpatterns = [
    path('', IndexProductView.as_view()),
]
