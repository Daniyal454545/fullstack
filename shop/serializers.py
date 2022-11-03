from .models import Shop
from rest_framework import serializers


class ShopSerializers(serializers.Serializer):
    class Meta:
        model = Shop
        fields = '__all__'