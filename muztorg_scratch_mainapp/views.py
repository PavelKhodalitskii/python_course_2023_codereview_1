from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
# Create your views here.

class MainPageView(TemplateView):
    template_name = "base.html"

class ProductList(ListView):
    template_name = ""