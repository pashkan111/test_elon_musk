from typing import Any

from django.contrib import admin
from django.db.models.query import QuerySet
from django.http import HttpRequest

from .models import Advantage, MenuItem


@admin.register(Advantage)
class AdvantageAdmin(admin.ModelAdmin):
    list_display = ("title", "value", "description", "is_displayed")
    search_fields = ("title", "value")
    ordering = ("order", "-is_displayed")


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ("title", "order", "is_displayed")
    search_fields = ("title",)
    ordering = ("order", "-is_displayed")
