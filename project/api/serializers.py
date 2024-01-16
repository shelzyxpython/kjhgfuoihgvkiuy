from rest_framework import serializers
from .models import Meal, Ingredients


# class MealSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Meal
#         fields = '__all__'

class MealSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=300)
    price = serializers.IntegerField()

    def create(self, validated_data):
        return Meal.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title),
        instance.description = validated_data.get('title', instance.description),
        instance.price = validated_data.get('title', instance.price)
        instance.save()
        return instance
