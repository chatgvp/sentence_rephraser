from rest_framework import serializers
from .models import Value


class ValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Value
        fields = ("id", "value")


class DogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Value
        fields = ("good_with_children", "good_with_other_dogs")
