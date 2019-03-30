from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import User, Delivery
from .serializers import UserSerializer, DeliverySerializer


class UserList(generics.ListCreateAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permissions_classes = (IsAuthenticated, )


class DeliveryList(generics.ListCreateAPIView):

    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer
