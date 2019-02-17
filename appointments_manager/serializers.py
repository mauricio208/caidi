from rest_framework import serializers
from appointments_manager.models import AppointmentRequest

class AppointmentRequestSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    parent_name = serializers.CharField(required=True, allow_blank=False, max_length=250)
    pacient_name = serializers.CharField(required=True, allow_blank=False, max_length=250)
    therapy_field = serializers.CharField(required=True, allow_blank=False, max_length=250)
    email = serializers.EmailField(max_length=254, required=True, allow_blank=False)
    phone_number = serializers.CharField(max_length=250, required=True, allow_blank=False)
    pacient_age = serializers.IntegerField(required=True)
    time_preference = serializers.CharField(max_length=2,required=True, allow_blank=False)



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
        instance.email = validated_data.get('email', instance.email)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.pacient_age = validated_data.get('pacient_age', instance.pacient_age)
        instance.time_preference = validated_data.get('time_preference', instance.time_preference)
        instance.save()
        return instance