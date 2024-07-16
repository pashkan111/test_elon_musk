from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from mainapp.models import Advantage, MenuItem

from .serializers import AdvantageReadSerializer, MenuItemReadSerializer


class AdvantageReadView(generics.ListAPIView):
    queryset = Advantage.objects.filter(is_displayed=True)
    serializer_class = AdvantageReadSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class MenuItemReadView(generics.ListAPIView):
    queryset = MenuItem.objects.filter(is_displayed=True)
    serializer_class = MenuItemReadSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
