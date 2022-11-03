from .models import SportCrud
from rest_framework import serializers


class SportCrudSerializers(serializers.Serializer):
    class Meta:
        model = SportCrud
        fields = '__all__'
