from django.urls import path
from blog.views import index, BlogCreateView
from blog.apps import BlogConfig

app_name = BlogConfig.name

urlpatterns = [
    path('', index, BlogCreateView.as_view(), name='blog_create')
]
