from django.urls import path
from .views import AdvantageReadView, MenuItemReadView


urlpatterns = [
    path('advantages/', AdvantageReadView.as_view(), name='advantages'),
    path('menu/', MenuItemReadView.as_view(), name='menu'),
]
