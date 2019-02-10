from rest_framework import serializers
from .models import Licensee, Violation


class ViolationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Violation
        fields = ('details', 'created_at', 'updated_at', 'updated_by')


class LicenseeSerializer(serializers.ModelSerializer):
    violations = ViolationSerializer(many=True)

    class Meta:
        model = Licensee
        fields = ('id', 'serial_number', 'licensee_name', 'details', 'mobile_number', 'licence_number', 'licence_status', 'issued_date', 'violations')
