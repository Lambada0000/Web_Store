from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy, reverse
from django.utils.text import slugify
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from blog.forms import BlogForm, BlogContentManagerForm
from blog.models import Blog


class BlogCreateView(CreateView):
    model = Blog
    fields = ('name', 'description', 'photo', 'is_published')
    success_url = reverse_lazy('blog:list')

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.name)
            new_blog.save()
        return super().form_valid(form)


class BlogListView(ListView):
    model = Blog

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views += 1
        self.object.save()
        return self.object


class BlogUpdateView(UpdateView):
    model = Blog
    fields = '__all__'
    success_url = reverse_lazy('blog:list')

    def get_success_url(self):
        return reverse('blog:blog_detail', args=[self.kwargs.get('pk')])

    def get_form_class(self):
        user = self.request.user
        if (
            user.has_perm("blog.can_add_blog_post")
        ):
            return BlogContentManagerForm
        raise PermissionDenied


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:list')
