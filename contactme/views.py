from django.shortcuts import render
from .serializers import ContactMessageSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.response import Response
from rest_framework import permissions

from.models import ContactMessage
# Create your views here.


class ContactMessageView(ModelViewSet ):
    serializer_class = ContactMessageSerializer
    def get_queryset(self):
        if self.request.method != 'POST' :
            permission_classes = [permissions.IsAdminUser]
            return ContactMessage.objects.all().order_by('-created_at')
        return None
    def perform_create(self, serializer):
        serializer.save()
        return Response({'detail' : 'Message Sent Successfully'},status=status.HTTP_200_OK)
    