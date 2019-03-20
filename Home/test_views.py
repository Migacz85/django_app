from django.shortcuts import reverse
from django.test import TestCase
from django.contrib.auth.models import User
from django.test import Client


class TestRegistration(TestCase):
    """Home page is using home.html template and is loading correctly"""

    def test_get_home_page(self):
        """Home page is loading home.html"""
        page = self.client.get("/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "home.html")

    def test_registration_is_using_register_html_template(self):
        """Register is using registration.html"""
        page = self.client.get("/accounts/register/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'registration.html')

    def test_registration_on_post(self):
        """Register link on post is returning status 200"""
        response = self.client.post("/accounts/register/", {
            'email': 'mig85gmailcom',
            'username': 'mig',
            'password1': 'pass',
            'password2': 'pass',
        })
        self.assertEqual(response.status_code, 200)


class TestLogin(TestCase):

    def test_login_on_post(self):
        """Login page on post is returning status 200"""
        response = self.client.post("/accounts/login/", {
            'username': 'mig',
            'password': 'pass',
        })
        self.assertEqual(response.status_code, 200)

    def test_login_page_redirect_logged_user(self):
        """Login page is redirecting to home page if user is logged in"""

        User.objects.create_user(username='Migacz', password='generic')
        client = Client()

        client.post('/accounts/login/', {
            'username': 'Migacz',
            'password': 'generic'
        })
        response = self.client.post("/accounts/login/", {
        })
        client.get('/accounts/login/', follow=True)

        response = client.get(reverse('login'))
        self.assertRedirects(
            response,
            expected_url=reverse('home'),
            status_code=302,
            target_status_code=200,
            fetch_redirect_response=True
        )
