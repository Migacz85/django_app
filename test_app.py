from django.apps import apps
from django.test import TestCase
from Home.apps import HomeConfig


class TestHomeConfig:
    """Checking Home """

    def test_app(self):
        self.assertEqual("Home", HomeConfig.name)
        self.assertEqual("Home", apps.get_app_config("Home"))
