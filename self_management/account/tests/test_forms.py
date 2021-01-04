from django.test import TestCase

from .. forms import SignUpForm


class UserFormTests(TestCase):
    def test_user_fail_blank_username(self):
        with self.assertRaises(TypeError):
            SignUpForm(
                username='',
                email='sample1@sample.com',
                password='testpass4321',
                ).is_valid()

    def test_user_fail_blank_email(self):
        with self.assertRaises(TypeError):
            SignUpForm(
                username='test_user1',
                email='',
                password='testpass4321',
                ).is_valid()

    def test_user_fail_blank_passward(self):
        with self.assertRaises(TypeError):
            SignUpForm(
                username='test_user1',
                email='sample1@sample.com',
                password=''
                ).is_valid()

    def test_user_fail_short_passward(self):
        with self.assertRaises(TypeError):
            SignUpForm(
                username='test_user1',
                email='sample1@sample.com',
                password='test123'
                ).is_valid()

    def test_user_fail_no_number_passward(self):
        with self.assertRaises(TypeError):
            SignUpForm(
                username='test_user1',
                email='sample1@sample.com',
                password='testpass',
                ).is_valid()
