from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView, UpdateView
from catalog.models import Product


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')


class ProductUpdateView(UpdateView):
    model = Product
    fields = ('name', 'description', 'price')
    success_url = reverse_lazy('catalog:product_list')
