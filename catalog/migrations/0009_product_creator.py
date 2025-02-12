# Generated by Django 4.2 on 2024-08-16 16:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("catalog", "0008_version"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="creator",
            field=models.ForeignKey(
                blank=True,
                help_text="Укажите создателя записи",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
                verbose_name="Создатель записи",
            ),
        ),
    ]
