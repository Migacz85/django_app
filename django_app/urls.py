"""django_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, re_path, include
from django.contrib import admin
from Home import urls as accounts_urls
from Home.views import home
from django.views.static import serve
from .settings import MEDIA_ROOT
from django.views.generic import RedirectView

urlpatterns = [
    re_path(r'^$', home, name="home"),
    path('admin/', admin.site.urls),
    re_path(r'^accounts/', include(accounts_urls)),
    # re_path(r'^$', RedirectView.as_view(url="bugs/")),
    re_path(r'bugs/', include('bugs.urls')),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
]
