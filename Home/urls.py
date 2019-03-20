from django.urls import path, re_path, include
from Home.views import logout, login, register, user_profile
from Home import url_reset

urlpatterns = [
    re_path(r'^logout/', logout, name="logout"),
    re_path(r'^login/', login, name="login"),
    re_path(r'^register/', register, name="register"),
    re_path(r'^profile/', user_profile, name="user_profile"),
    path('', include(url_reset))
]
