from django.urls import re_path
from .views import get_bugs, get_bug_detail, create_or_edit_bug
from .views import upvote_bug, add_comment_bugs

urlpatterns = [
    re_path(r'^$', get_bugs, name='get_bugs'),
    re_path(r'^(?P<pk>\d+)/$', get_bug_detail, name='get_bug_detail'),
    re_path(r'^new/$', create_or_edit_bug, name='new_bug'),
    re_path(r'^(?P<pk>\d+)/edit/$', create_or_edit_bug, name='edit_bug'),
    re_path(r'^(?P<pk>\d+)/upvote/$', upvote_bug, name='upvote_bug'),
    re_path(r'^(?P<pk>\d+)/add/$', add_comment_bugs, name='add_comment_bugs'),
]