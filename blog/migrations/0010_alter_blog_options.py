# Generated by Django 4.2 on 2024-08-20 10:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0009_blog_updated_at"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="blog",
            options={
                "permissions": [
                    ("can_add_blog_post", "Can add blog post"),
                    ("can_edit_blog_name", "Can edit blog name"),
                    ("can_edit_blog_description", "Can edit blog description"),
                    ("can_edit_blog_photo", "Can edit blog photo"),
                    ("can_edit_blog_is_published", "Can edit blog is published"),
                ],
                "verbose_name": "Запись",
                "verbose_name_plural": "Записи",
            },
        ),
    ]
