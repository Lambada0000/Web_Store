from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from catalog.models import Product


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


# CreateRUD
class ProductCreateView(CreateView):
    model = Product
    fields = ('name')
    success_url = reverse_lazy('catalog:product_list')
