from django.urls import path

from .views import AdvantageReadView, MenuItemReadView

urlpatterns = [
    path("advantages/", AdvantageReadView.as_view(), name="advantages-list"),
    path("menu/", MenuItemReadView.as_view(), name="menuitem-list"),
]
