from rest_framework import serializers
from models import AppointmentRequest

class AppointmentRequestSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    parent_name = serializers.CharField(required=False, allow_blank=True, max_length=100)
    pacient_name = serializers.CharField(required=False, allow_blank=True, max_length=100)
    therapy_field = serializers.CharField(required=False, allow_blank=True, max_length=100)

    def create(self, validated_data):
        """
        Create and return a new `AppointmentRequest` instance, given the validated data.
        """
        return AppointmentRequest.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `AppointmentRequest` instance, given the validated data.
        """
        instance.parent_name = validated_data.get('parent_name', instance.parent_name)
        instance.pacient_name = validated_data.get('pacient_name', instance.pacient_name)
        instance.therapy_field = validated_data.get('therapy_field', instance.therapy_field)
        instance.save()
        return instance