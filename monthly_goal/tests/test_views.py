from django.test import TestCase
from django.contrib.auth import get_user_model
# Create your tests here.


class TestSignInView(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='test1', email='samples@sample.com', password='1234pass'
        )

    def test_get_signup_post_success(self):
        self.client.login(username='test1', password='1234pass')
        response = self.client.get('/main/')
        self.assertTrue(response)
