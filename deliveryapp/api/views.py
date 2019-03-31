from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from . import models
from . import serializers


class UserList(generics.ListCreateAPIView):

    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer


class DeliveryList(generics.ListCreateAPIView):

    queryset = models.Delivery.objects.all()
    serializer_class = serializers.DeliverySerializer


class DeliveryDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = models.Delivery.objects.all()
    serializer_class = serializers.DeliverySerializer


class OrderList(generics.ListCreateAPIView):

    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer
    permissions_classes = (IsAuthenticated, )


class OrderDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer


class PaymentList(generics.ListCreateAPIView):

    queryset = models.Payment.objects.all()
    serializer_class = serializers.PaymentSerializer


class PaymentDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = models.Payment.objects.all()
    serializer_class = serializers.PaymentSerializer


class TripList(generics.ListCreateAPIView):

    queryset = models.Trip.objects.all()
    serializer_class = serializers.TripSerializer


class TripDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = models.Trip.objects.all()
    serializer_class = serializers.TripSerializer


class RatingList(generics.ListCreateAPIView):

    queryset = models.Rating.objects.all()
    serializer_class = serializers.RatingSerializer


class RatingDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = models.Rating.objects.all()
    serializer_class = serializers.RatingSerializer
