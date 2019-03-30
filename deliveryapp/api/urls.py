from django.conf.urls import url
from django.urls import include, path
from rest_framework_jwt.views import obtain_jwt_token
from . import views

urlpatterns = [
    path('login/', obtain_jwt_token),

    url(r'^users/$', views.UserList.as_view(), name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name='user-detail'),

    url(r'^deliverys/$', views.DeliveryList.as_view(), name='delivery-list'),
    url(r'^deliverys/(?P<pk>[0-9]+)/$', views.DeliveryDetail.as_view(), name='delivery-detail'),

    url(r'^orders/$', views.OrderList.as_view(), name='order-list'),
    url(r'^orders/(?P<pk>[0-9]+)/$', views.OrderDetail.as_view(), name='order-detail'),

    url(r'^trips/$', views.TripList.as_view(), name='trip-list'),
    url(r'^trips/(?P<pk>[0-9]+)/$', views.TripDetail.as_view(), name='trip-detail'),

    url(r'^payments/$', views.PaymentList.as_view(), name='payment-list'),
    url(r'^payments/(?P<pk>[0-9]+)/$', views.PaymentDetail.as_view(), name='payment-detail'),

    url(r'^ratings/$', views.RatingList.as_view(), name='rating-list'),
    url(r'^ratings/(?P<pk>[0-9]+)/$', views.RatingDetail.as_view(), name='rating-detail'),
]
