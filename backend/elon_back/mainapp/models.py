from django.db import models


class Advantage(models.Model):
    title = models.CharField(
        max_length=100,
        help_text="Заголовок для админки (на фронте не будет отображаться)",
        null=True,
    )
    value = models.CharField(max_length=100)
    description = models.CharField(
        max_length=100, help_text="Значком % обозначьте перенос строки в тексте"
    )
    is_displayed = models.BooleanField(default=True, help_text="Отображать ли блок")
    order = models.IntegerField(help_text="Порядок следования", unique=True)

    def __str__(self):
        return self.title


class MenuItem(models.Model):
    title = models.CharField(max_length=100)
    order = models.IntegerField(help_text="Порядок следования", unique=True)
    is_displayed = models.BooleanField(
        default=True, help_text="Отображать ли пункт меню"
    )

    def __str__(self):
        return self.title
