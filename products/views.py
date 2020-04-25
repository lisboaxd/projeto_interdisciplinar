from django.shortcuts import render
from django.views.generic import TemplateView, ListView
class ListProductView(TemplateView):
    template_name = "list.html"


class CreateProductView(TemplateView):
    template_name = "create.html"