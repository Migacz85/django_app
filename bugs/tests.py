from django.shortcuts import get_object_or_404
from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import Issues


class TestViews(TestCase):

    def setUp(self):
        self.user = User.objects.create(
            username='admin',
            password='asdfg',
            is_active=True,
            is_staff=True,
            is_superuser=True
        )
        self.user.set_password("asdfg")
        self.user.save()

        self.user = User.objects.create(
            username='John',
            password='asdfg',
            is_active=True,
            is_staff=True,
            is_superuser=False
        )
        self.user.set_password("asdfg")
        self.user.save()

        self.client = Client()
        self.issue = Issues.objects.create(
            title='test',
            content='this is a test',
            username=self.user
        )
        self.issue.save()

    def test_upvote_issue(self):
        self.client.login(username='admin', password='asdfg')
        response = self.client.get('/issues/{0}/upvote/'.format(self.issue.id))
        item = get_object_or_404(Issues, pk=1)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(item.content, "this is a test")
        self.assertEqual(item.upvotes, 1)

    def test_upvoting_same_issue_using_2_different_users(self):

        # So john logged to the site
        self.client.login(username='John', password='asdfg')
        # And he decided to upvote issue number 1
        response = self.client.get('/issues/{0}/upvote/'.format(self.issue.id))
        # And after that he logout and go out for smoke
        self.client.get('/accounts/logout/')
        # Then admin came in and logged as normal user
        response2 = self.client.post('/accounts/login/', {
            'username': "admin",
            'password': 'asdfg'}
        )
        # He navigate to the same issue as John and upvoted same issue
        response = self.client.get('/issues/{0}/upvote/'.format(self.issue.id))
        item = get_object_or_404(Issues, pk=1)

        self.assertEqual(response.status_code, 302)
        self.assertEqual("admin", str(response2.wsgi_request.user))
        self.assertEqual(item.upvotes, 2)
