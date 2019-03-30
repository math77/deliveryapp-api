from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from . import models
from . import serializers


class UserList(generics.ListCreateAPIView):

    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
    permissions_classes = (IsAuthenticated, )


class DeliveryList(generics.ListCreateAPIView):

    queryset = models.Delivery.objects.all()
    serializer_class = serializers.DeliverySerializer


class OrderList(generics.ListCreateAPIView):

    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer
    permissions_classes = (IsAuthenticated, )


class PaymentList(generics.ListCreateAPIView)::

    queryset = models.Payment.objects.all()
    serializer_class = serializers.PaymentSerializer


class TripList(generics.ListCreateAPIView):

    queryset = models.Trip.objects.all()
    serializer_class = serializers.TripSerializer


class RatingList(generics.ListCreateAPIView):

    queryset = models.Rating.objects.all()
    serializer_class = serializers.Rating
