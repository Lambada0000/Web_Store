from django.urls import path
from blog.views import index
from blog.apps import BlogConfig

app_name = BlogConfig.name

urlpatterns = [
    path('', index,)
]
