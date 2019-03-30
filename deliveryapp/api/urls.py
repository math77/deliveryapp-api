from django.conf.urls import url
from django.urls import include, path
from rest_framework_jwt.views import obtain_jwt_token
from . import views

urlpatterns = [
    path('login/', obtain_jwt_token),
    url(r'^users/$', views.UserList.as_view(), name='user-list'),
    url(r'^deliverys/$', views.DeliveryList.as_view(), name='delivery-list'),
]
