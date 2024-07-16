from django.db import models

class Advantage(models.Model):
    title = models.CharField(
        max_length=100, 
        help_text="Заголовок для админки (на фронте не будет отображаться)",
        null=True
    )
    value = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    is_displayed = models.BooleanField(default=True, help_text="Отображать ли блок")

    def __str__(self):
        return self.title


class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    order = models.IntegerField(default=0, help_text="Порядок следования")
    is_displayed = models.BooleanField(default=True, help_text="Отображать ли пункт меню")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['order']