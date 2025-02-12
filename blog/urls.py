from django.urls import path
from blog.apps import BlogConfig
from blog.views import BlogCreateView, BlogListView, BlogDetailView, BlogUpdateView, BlogDeleteView

app_name = BlogConfig.name

urlpatterns = [
    path('', BlogListView.as_view(), name='list'),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='detail'),
    path('create/', BlogCreateView.as_view(), name='create'),
    path('blog/<int:pk>/update', BlogUpdateView.as_view(), name='update'),
    path('blog/<int:pk>/delete/', BlogDeleteView.as_view(), name='delete'),
]