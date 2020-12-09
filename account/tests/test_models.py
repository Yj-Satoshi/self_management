from django.test import TestCase
from django.db.utils import IntegrityError

from .factory import CustomUserFactory
from .. forms import SignUpForm

# import logging
# logger = logging.getLogger('django_test')
# logger.info('test_log')

# Create your tests here.


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

    def test_user_fail_nonumber_passward(self):
        # with form.is_valid().assertRaises(IntegrityError):
        #     CustomUserFactory(password='testpass')
        with self.assertRaises(IntegrityError):
            CustomUserFactory(password='testpass')
        # self.assertTrue(CustomUserFactory(password='testpass'))
        # self.assertFalse(SignUpForm(data=CustomUserFactory(password='testpass')).is_valid())

    # def test_user_fail_blank_username(self):
    #     with self.assertRaises(Error):
    #         CustomUserFactory(username='')

    def test_user_fail_blank_email(self):
        with self.assertRaises(IntegrityError):
            CustomUserFactory(email='')

    def test_user_fail_blank_passward(self):
        with self.assertRaises(IntegrityError):
            CustomUserFactory(password='')
