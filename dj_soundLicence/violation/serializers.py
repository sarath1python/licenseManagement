from rest_framework import serializers
from .models import License, Violation


class ViolationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Violation
        fields = ('details', 'created_at', 'updated_at', 'updated_by')


class LicenseSerializer(serializers.ModelSerializer):
    violations = ViolationSerializer(many=True)

    class Meta:
        model = License
        fields = ('id', 'serial_number', 'name', 'details', 'mobile_number', 'number', 'status', 'issued_date', 'violations')
