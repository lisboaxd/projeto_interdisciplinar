from django.shortcuts import render
from django.views.generic import TemplateView
class IndexProductView(TemplateView):
    template_name = "list.html"