from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from blog.models import Blog


def index(request):
    return render(request, 'blog/base.html')


class BlogCreateView(CreateView):
    model = Blog
    fields = '__all__'
    success_url = reverse_lazy('catalog:product_list')
