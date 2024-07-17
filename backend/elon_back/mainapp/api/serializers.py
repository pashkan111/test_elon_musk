from rest_framework import serializers

from mainapp.models import Advantage, MenuItem


class AdvantageReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advantage
        fields = ("value", "description")


class MenuItemReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ("title",)
