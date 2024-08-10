from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="Наименование категории",
        help_text="Введите наименование категории",
    )
    description = models.TextField(
        verbose_name="Описание категории",
        help_text="Введите описание категории",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="Наименование продукта",
        help_text="Введите наименование продукта",
    )
    slug = models.CharField(
        max_length=50,
        verbose_name="Ссылка",
        help_text="Введите ссылку",
    )
    description = models.TextField(
        max_length=500,
        verbose_name="Описание продукта",
        help_text="Введите описание продукта",
        blank=True,
        null=True,
    )
    photo = models.ImageField(
        upload_to="product/photo",
        blank=True,
        null=True,
        verbose_name="Изображение продукта",
        help_text="Загрузите фото продукта",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name="Категория",
        help_text="Введите категорию",
        null=True,
        blank=True,
        related_name="categories",
    )
    price = models.PositiveIntegerField(
        blank=True, null=True, verbose_name="Цена", help_text="Укажите цену за покупку"
    )
    created_at = models.DateField(
        blank=True,
        null=True,
        auto_now_add=True,
        verbose_name="Дата создания",
        help_text="Укажите дату создания записи",
    )
    updated_at = models.DateField(
        blank=True,
        null=True,
        auto_now=True,
        verbose_name="Дата последнего изменения",
        help_text="Укажите дату последнего изменения записи",
    )
    views = models.PositiveIntegerField(
        default=0,
        verbose_name="Количество просмотров",
        help_text="Укажите количество просмотров",
    )

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name", "category", "price", "created_at"]

    def __str__(self):
        return self.name


class Version(models.Model):
    product = models.ForeignKey(
        Product,
        related_name="versions",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Продукт",
        help_text="Выберите продукт",
    )
    version_number = models.CharField(
        max_length=10,
        null=True,
        blank=True,
        verbose_name="Номер версии",
        help_text="Введите номер версии",
    )
    version_name = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name="Название версии",
        help_text="Введите название версии",
    )
    is_version_active = models.BooleanField(
        default=False,
        verbose_name="Активная версия",
        help_text="Является ли версия активной?",
    )

    class Meta:
        verbose_name = "Версия"
        verbose_name_plural = "Версии"
        ordering = ["version_number", "version_name"]

    def __str__(self):
        return self.version_name
