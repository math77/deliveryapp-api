from django.conf.urls import url
from django.urls import include, path
from rest_framework_jwt.views import obtain_jwt_token
from . import views

urlpatterns = [
    path('login/', obtain_jwt_token),
    url(r'^users/$', views.UserList.as_view(), name='user-list'),
    url(r'^deliverys/$', views.DeliveryList.as_view(), name='delivery-list'),
    url(r'^orders/$', views.OrderList.as_view(), name='order-list'),
    url(r'^trips/$', views.TripList.as_view(), name='trip-list'),
    url(r'^payments/$', views.PaymentList.as_view(), name='payment-list'),
    url(r'^ratings/$', views.RatingList.as_view(), name='rating-list'),
]
