from rest_framework import serializers
from .models import User, Delivery


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'first_name', 'last_name', 'cpf', 'phone')



class DeliverySerializer(serializers.ModelSerializer):

    class Meta:
        model = Delivery
        fields = '__all__'
