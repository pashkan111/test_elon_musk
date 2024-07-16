from typing import Any

from django.contrib import admin
from django.db.models.query import QuerySet
from django.http import HttpRequest

from .models import Advantage, MenuItem


@admin.register(Advantage)
class AdvantageAdmin(admin.ModelAdmin):
    list_display = ("title", "value", "description", "is_displayed")
    search_fields = ("title", "value")

    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        return super().get_queryset(request).order_by("-is_displayed")


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ("name", "order", "is_displayed")
    search_fields = ("name",)
    ordering = ("order",)

    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        return super().get_queryset(request).order_by("-is_displayed")
