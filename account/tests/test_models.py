from django.test import TestCase
from django.db.utils import IntegrityError

from .factory import CustomUserFactory

# import logging
# logger = logging.getLogger('django_test')
# logger.info('test_log')


class UserTests(TestCase):
    def setUp(self):
        self.user1 = CustomUserFactory()
        self.user2 = CustomUserFactory(
            username='test_user',
            email='sample@sample.com',
            password='testpass1234')

    def test_user(self):
        self.assertTrue(self.user1)

    def test_user_fail_same_username(self):
        with self.assertRaises(IntegrityError):
            CustomUserFactory(username='test_user')

