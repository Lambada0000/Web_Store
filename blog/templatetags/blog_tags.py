from django import template

register = template.Library()


@register.filter()
def media_filter(path):
    if path:
        return f"/media/product/photo/{path}"
    return "#"