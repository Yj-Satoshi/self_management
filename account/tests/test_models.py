from django.test import TestCase
from . factory import CustomUserFactory
# Create your tests here.


class UserTests(TestCase):

    def setUp(self):
        self.user1 = CustomUserFactory()
        self.user2 = CustomUserFactory(username='test_user')

    def testUser(self):
        self.assertTrue(self.user1, self.user2)
