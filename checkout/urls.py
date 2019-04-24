from django.conf.urls import url, re_path
from .views import checkout, cart_success

urlpatterns = [
    url(r'^$', checkout, name="checkout"),
    url(r'cart_success/$', cart_success, name="cart_success"),
]
