from django.shortcuts import render

# Create your views here.
from .models import CustomUser
from rest_framework import viewsets,permissions
from .serializers import UserSerializer


class UserViewset(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [permissions.IsAuthenticated]




