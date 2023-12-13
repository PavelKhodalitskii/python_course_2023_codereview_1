from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView

from .models import Product
from  .scratch import Scratch
from .utils import get_best_deals

class MainPageView(ListView):
    model = Product
    context_object_name = "products"
    template_name = "mainpage.html"

    def get_queryset(self) -> QuerySet[Any]:
        best_deals = get_best_deals()
        print(best_deals)
        return best_deals

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
        queryset = scratch.get_data_by_cat(category_slug, page_number)
        # if category_slug:
        #     queryset = queryset.filter(category=category_slug)
        return queryset
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        category_slug = self.kwargs[self.slug_url_kwarg]
        page_number = self.kwargs[self.page_number_kwarg]
        prev_page = str(int(page_number) - 1)
        next_page = str(int(page_number) + 1)
        c_def = {"base_ur": "photos/rockdale-stars-hss-bk0.jpg", "next_page": next_page, "prev_page": prev_page, "category_slug": category_slug}
        return dict(list(context.items()) + list(c_def.items()))
    
class ProductDetailView(DetailView):
    model = Product
    template_name = "detail_view.html"
    slug_url_kwarg = 'product_slug'
    context_object_name = 'product'
