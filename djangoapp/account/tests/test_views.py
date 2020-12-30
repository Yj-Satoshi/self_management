from django.test import TestCase

from django.contrib.auth import get_user_model

# Create your tests here.


class TestSignInView(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='test1', email='samples@sample.com', password='1234pass'
        )

    def test_get_signup_page_success(self):
        response = self.client.get('/signup/')
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.context['form'].errors)
        self.assertTemplateUsed(response, 'account/signup.html')

    def test_get_signin_post_success(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.context['form'].errors)
        self.assertTemplateUsed(response, 'account/index.html')

    def test_get_signup_post_success(self):
        self.client.post('/signup/', {
            'username': 'testuser',
            'email': 'sample@sample.com',
            'password': 'testpass1234',
            'password2': 'testpass1234',
        })
        self.client.login(username='testuser', password='testpass1234')
        response = self.client.get('/main/')
        self.assertTrue(response)
