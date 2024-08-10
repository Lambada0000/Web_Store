from django import template
from django.conf import settings

register = template.Library()


@register.filter()
def media_filter(photo, product):
    if photo:
        return f"{settings.MEDIA_URL}{photo}"
    if product.category.pk == 1:
        return f"{settings.MEDIA_URL}product/photo/default/default_notebook.png"
    elif product.category.pk == 2:
        return f"{settings.MEDIA_URL}product/photo/default/default_monitor.png"
