from .models import ContactMessage
from rest_framework import serializers


class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = '__all__'
        read_only_fields = ['id']
        extra_kwargs = {
            'email': {'required': True},
            'name': {'required': True},
            'message': {'required': True},
        }