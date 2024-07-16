from django.contrib import admin
from .models import Advantage, MenuItem


@admin.register(Advantage)
class AdvantageAdmin(admin.ModelAdmin):
    list_display = ('title', 'value', 'description', 'is_displayed')
    search_fields = ('title', 'value')


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'order', 'is_displayed')
    search_fields = ('name',)
    ordering = ('order',)
