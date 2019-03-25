from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from .managers import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(_('username'), max_length=30, unique=True)
    first_name = models.CharField(_('First Name'), max_length=30, null=False, blank=False)
    last_name = models.CharField(_('Last Name'), max_length=30, null=False, blank=False)
    email = models.EmailField(_('email address'), unique=True)
    cpf = models.CharField(max_length=11, null=False, blank=False, unique=True)
    phone = models.CharField(max_length=13, null=False, blank=False)
    about = models.CharField(max_length=150)
    criminal_background_check_pic = models.ImageField(upload_to='pic_folder/')
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(null=False, auto_now_add=True)
    profile_pic = models.ImageField(upload_to='pic_profile_folder/')


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'cpf', 'phone', 'username']

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Payment(models.Model):

    token = models.CharField(max_length=80, null=False, blank=False)
    confirmed = models.BooleanField(default=False)
    confirmation_date = models.DateTimeField()


class TypeLocomotion(models.Model):

    description = models.CharField(max_length=30, null=False, blank=False)



class Trip(models.Model):

    completed = models.BooleanField(default=False)
    created = models.DateTimeField(null=False, auto_now_add=True)
    id_type_locomotion = models.ForeignKey(TypeLocomotion, on_delete=models.DO_NOTHING)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()


class Delivery(models.Model):

    price = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(null=False, auto_now_add=True)
    id_payment = models.OneToOneField(Payment, on_delete=models.CASCADE)
    id_trip = models.ForeignKey(Trip, on_delete=models.DO_NOTHING)


class Order(models.Model):

    initial_latitude = models.FloatField(null=False)
    initial_longitude = models.FloatField(null=False)
    final_latitude = models.FloatField(null=False)
    final_longitude = models.FloatField(null=False)
    created = models.DateTimeField(null=False, auto_now_add=True)
    delivered = models.BooleanField(default=False)
    id_delivery = models.ForeignKey(Delivery, on_delete=models.DO_NOTHING)
    id_user_sender = models.ForeignKey(User, on_delete=models.DO_NOTHING)



class Rating(models.Model):

    rating = models.IntegerField()
    comment = models.TextField()
    id_user_evaluated = models.ForeignKey(User, related_name='user_evaluated', on_delete=models.DO_NOTHING)
    id_user_appraiser = models.ForeignKey(User, related_name='user_appraiser', on_delete=models.DO_NOTHING)


objects = models.Manager()
