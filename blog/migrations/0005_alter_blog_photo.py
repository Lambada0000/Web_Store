# Generated by Django 5.0.6 on 2024-08-08 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0004_alter_blog_photo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="photo",
            field=models.ImageField(
                blank=True,
                default="media/product/photo/default_blog.png",
                help_text="Загрузите изображение",
                null=True,
                upload_to="product/photo",
                verbose_name="Изображение",
            ),
        ),
    ]
