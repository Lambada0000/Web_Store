# Generated by Django 5.0.6 on 2024-08-09 09:59

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0004_product_views"),
    ]

    operations = [
        migrations.RenameField(
            model_name="product",
            old_name="image",
            new_name="photo",
        ),
        migrations.AddField(
            model_name="product",
            name="slug",
            field=models.CharField(
                default=django.utils.timezone.now,
                help_text="Введите ссылку",
                max_length=50,
                verbose_name="Ссылка",
            ),
            preserve_default=False,
        ),
    ]
