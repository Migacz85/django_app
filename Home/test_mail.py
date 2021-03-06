from django.core import mail
from django.test import TestCase


class EmailTest(TestCase):
    def test_send_email(self):
        """ Test if the sending message is correct
        """
        mail.send_mail(
            'Subject here',
            'Here is the message.',
            'from@example.com',
            ['to@example.com'],
            fail_silently=False)

        # Test that one message has been sent.

        self.assertEqual(len(mail.outbox), 1)
