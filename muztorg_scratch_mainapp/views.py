from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView

from .models import Product
from  .scratch import Scratch

class MainPageView(TemplateView):
    template_name = "mainpage.html"

class ProductList(ListView):
    model = Product
    template_name = "productlist.html"
    slug_url_kwarg = 'category_slug'
    page_number_kwarg = 'page_number'
    context_object_name = "products"

    def get_queryset(self) -> QuerySet[Any]:
        category_slug = self.kwargs[self.slug_url_kwarg]
        page_number = self.kwargs[self.page_number_kwarg]
        scratch = Scratch()
        scratch.get_data_by_cat(category_slug, page_number)
        queryset = super().get_queryset()
        if category_slug:
            queryset = queryset.filter(category=category_slug)
        return queryset
    
class ProductDetailView(DetailView):
    model = Product
    template_name = "detail_view.html"
    slug_url_kwarg = 'product_slug'
    context_object_name = 'product'
