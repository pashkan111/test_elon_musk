from django.contrib import admin
from .models import Advantage, MenuItem


@admin.register(Advantage)
class AdvantageAdmin(admin.ModelAdmin):
    list_display = ('title', 'value', 'description')
    search_fields = ('title', 'value')


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'order')
    search_fields = ('name',)
    ordering = ('order',)
