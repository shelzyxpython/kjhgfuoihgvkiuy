from rest_framework import serializers
from .models import *


class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = 'all'


class ProductSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=10)
    size = serializers.IntegerField()
    price = serializers.IntegerField()

    def create(self, validated_data):
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.size = validated_data.get('size', instance.size)
        instance.price = validated_data.get('price', instance.price)
        instance.save()
        return instance