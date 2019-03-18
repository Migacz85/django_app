from django.test import TestCase
from .forms import UserLoginForm, UserRegistrationForm

class TestLoginForm(TestCase):
    """Test for Login form"""

    def test_can_input_password_and_username(self):
        """Form is valid only when user enter name and password"""
        form = UserLoginForm({'username': 'Tom', 'password': 'password'})
        self.assertTrue(form.is_valid())

    def test_can_not_input_username_without_password(self):
        """Form is not valid when user don't enter a password"""
        form = UserLoginForm({'username': 'Tom', 'password': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['password'], ['This field is required.'])


class TestRegistrationForm(TestCase):
    """Test for matching passwords in  registration form"""

    def test_password_must_match(self):
        form = UserRegistrationForm({
            'email': 'mig85@gmail.com',
            'username': 'mig',
            'password1': 'pass2',
            'password2': 'pass',
        })
        self.assertFalse(form.is_valid())

    def test_mail_is_not_valid_without_a_dot(self):
        form = UserRegistrationForm({
            'email': 'mig85gmailcom',
            'username': 'mig',
            'password1': 'pass',
            'password2': 'pass',
        })
        self.assertFalse(form.is_valid())

    def test_mail_is_not_valid_without_at_symbol(self):
        form = UserRegistrationForm({
            'email': 'mig85gmail.com',
            'username': 'mig',
            'password1': 'pass',
            'password2': 'pass',
        })
        self.assertFalse(form.is_valid())
