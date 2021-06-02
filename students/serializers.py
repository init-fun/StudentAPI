from rest_framework.exceptions import ValidationError
from .models import Student
from rest_framework import serializers


class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    city = serializers.CharField(max_length=100)
    roll = serializers.IntegerField()

    def create(self, validate_data):
        return Student.objects.create(**validate_data)

    def update(self, instance, validated_data):
        # instance - old data
        # validated_data = new_Data
        instance.name = validated_data.get("name", instance.name)
        instance.roll = validated_data.get("roll", instance.roll)
        instance.city = validated_data.get("city", instance.city)

        instance.save()
        return instance

    # VALIDATORS
    def validate_roll(self, value):
        if value >= 200:
            raise ValidationError("Seat full")
        return value

    def validate(self, data):
        nm = data.get("name")
        ct = data.get("city")
        if nm.lower() == "kapil" and ct.lower() != "bengaluru":
            raise ValidationError("City must be bengaluru")
        return data
