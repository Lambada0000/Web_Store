from django.db import models
from django.conf import settings


class Blog(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="Заголовок",
        help_text="Введите заголовок",
    )
    slug = models.CharField(
        max_length=50,
        verbose_name="Ссылка",
        help_text="Введите ссылку",
    )
    description = models.TextField(
        verbose_name="Содержимое",
        help_text="Введите содержимое",
        blank=True,
        null=True,
    )
    photo = models.ImageField(
        upload_to="product/photo",
        blank=True,
        null=True,
        verbose_name="Изображение",
        help_text="Загрузите изображение",
    )
    created_at = models.DateTimeField(
        blank=True,
        null=True,
        auto_now_add=True,
        verbose_name="Дата создания",
        help_text="Укажите дату создания",
    )
    is_published = models.BooleanField(
        default=False,
        verbose_name="Опубликовано",
        help_text="Опубликовать запись",
    )
    views = models.PositiveIntegerField(
        default=0,
        verbose_name="Количество просмотров",
        help_text="Укажите количество просмотров",
    )

    def __str__(self):
        return self.name

    # def get_image_url(self):
    #     if self.photo:
    #         return self.photo.url
    #     else:
    #         return f'{settings.MEDIA_URL}product/photo/default.jpg'

    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Записи"
