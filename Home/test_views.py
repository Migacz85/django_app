from django.shortcuts import reverse, get_object_or_404
from django.test import TestCase, Client
from django.contrib.auth.models import User


class TestHomePage(TestCase):
    """Tests for home page """

    def test_get_home_page(self):
        """Home page is loading home.html"""
        page = self.client.get("/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "home.html")


class TestRegistration(TestCase):
    """Home page is using home.html template and is loading correctly"""

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

    def test_registering_new_user(self):
        """Register page can create an new user when details are valid"""
        response = self.client.post('/accounts/register/', {
            'username': 'user',
            'email': 'user@test.com',
            'password1': 'testtest',
            'password2': 'testtest'
        })
        user = get_object_or_404(User, username="user")
        print(response)

        self.assertEqual(str(user), "user")

    # def test_same_username_can_not_register(self):
    #     self.user = User.objects.create_user(username='user123',
    #                                          email='user@test.com',
    #                                          password='testtest')
    #     self.user.save()
    #     self.client.post('/accounts/logout/')
    #     response = self.client.post('/accounts/register/',
    #                                 {
    #                                     'username': 'user123',
    #                                     'email': 'user@test.com',
    #                                     'password1': 'testtest',
    #                                     'password2': 'testtest'
    #                                 })
    #     self.assertIn('A user with that username already exists.',
    #                   str(response.content))


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
