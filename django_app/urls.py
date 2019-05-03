# Main Django url config

from django.urls import path, re_path, include
from django.contrib import admin
from Home import urls as accounts_urls
from Home.views import home
from django.views.static import serve
from .settings import MEDIA_ROOT
from cart import urls as urls_cart
from checkout import urls as urls_checkout
from charts.views import charts

urlpatterns = [
    re_path(r'^$', home, name="home"),
    path('admin/', admin.site.urls),
    re_path(r'^charts/', charts, name="charts"),

    re_path(r'^accounts/', include(accounts_urls)),
    re_path(r'issues/', include('bugs.urls')),
    re_path(r'^cart/', include(urls_cart)),
    re_path(r'^checkout/', include(urls_checkout)),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
]
