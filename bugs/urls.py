from django.urls import re_path
from .views import get_bugs, get_issue_detail, create_or_edit_issue
from .views import upvote_issue, add_comment_issue, get_features

urlpatterns = [
    re_path(r'bugs$', get_bugs, name='get_bugs'),
    re_path(r'features$', get_features,  name='get_features'),
    re_path(r'^(?P<pk>\d+)/$', get_issue_detail, name='get_bug_detail'),
    re_path(r'^new/$', create_or_edit_issue, name='new_bug'),
    re_path(r'^(?P<pk>\d+)/edit/$', create_or_edit_issue, name='edit_bug'),
    re_path(r'^(?P<pk>\d+)/upvote/$', upvote_issue, name='upvote_bug'),
    re_path(r'^(?P<pk>\d+)/add/$', add_comment_issue, name='add_comment_bugs'),
]
