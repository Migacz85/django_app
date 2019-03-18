from django.test import TestCase


class TestViews(TestCase):
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

    def test_registration_on_post(self):
        """Register link on post is returning status 200"""
        response = self.client.post("/accounts/register/", {
            'email': 'mig85gmailcom',
            'username': 'mig',
            'password1': 'pass',
            'password2': 'pass',
        })

        self.assertEqual(response.status_code, 200)
