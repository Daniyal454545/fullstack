from rest_framework import serializers
from django.db.models import Avg
from category.models import Category
from .models import Person


class PersonListSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')

    class Meta:
        model = Person
        fields = (
            'name',
            'lastname',
            'age',
            'height',
            'weight',
            'group_blood',
            'allergy',
            'symptoms',
            'disability',
            'injury',
            'illness',
            'person_images',
        )

    def to_representation(self, instance):
        drs = super().to_representation(instance)
        print(instance,
              '***'
              )
        drs['rating'] = instance.reviews.aggregate(Avg('rating'))['rating__avg']
        return drs


class PersonDetailSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(
        source='owner.email'
    )
    category = serializers.PrimaryKeyRelatedField(
        required=True, queryset=Category.objects.all()
    )


    class Meta:
        model = Person
        fields = '__all__'

    def to_representation(self, instance):
        drs = super().to_representation(instance)
        drs['rating'] = instance.reviews.aggregate(Avg('rating'))['rating__avg']
        drs['rating_count'] = instance.reviews.count()
        return drs

