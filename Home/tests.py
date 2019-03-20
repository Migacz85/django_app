from django.test import TestCase


class TestDjango(TestCase):
    """This is example of simple test"""

    def test_is_this_thing_one(self):
        self.assertEqual(1, 1)
