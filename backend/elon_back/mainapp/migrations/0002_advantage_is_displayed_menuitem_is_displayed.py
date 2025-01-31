# Generated by Django 5.0.7 on 2024-07-16 17:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("mainapp", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="advantage",
            name="is_displayed",
            field=models.BooleanField(default=True, help_text="Отображать ли блок"),
        ),
        migrations.AddField(
            model_name="menuitem",
            name="is_displayed",
            field=models.BooleanField(
                default=True, help_text="Отображать ли пункт меню"
            ),
        ),
    ]
