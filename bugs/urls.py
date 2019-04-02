from django.urls import re_path
from .views import get_bugs, get_bug_detail, create_or_edit_bug

urlpatterns = [
    re_path(r'^$', get_bugs, name='get_bugs'),
    re_path(r'^(?P<pk>\d+)/$', get_bug_detail, name='get_bug_detail'),
    re_path(r'^new/$', create_or_edit_bug, name='new_bug'),
    re_path(r'^(?P<pk>\d+)/edit/$', create_or_edit_bug, name='edit_bug')
]
