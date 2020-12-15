from django.test import TestCase

from django.contrib.auth import get_user_model

# Create your tests here.


class TestSignInView(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='test1', email='samples@sample.com', password='1234pass'
        )

    def test_get_success(self):
        response = self.client.get('/signup/')
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.context['form'].errors)
        self.assertTemplateUsed(response, 'account/signup.html')
