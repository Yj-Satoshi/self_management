from django.test import TestCase
from django.db.utils import IntegrityError

from .factory import CustomUserFactory
from .factory import MonthlyGoalFactory

# import logging
# logger = logging.getLogger('django_test')
# logger.info('test_log')


class MonthlyGoalTests(TestCase):
    def setUp(self):
        self.user1 = CustomUserFactory()
        self.user2 = CustomUserFactory(
            username='test_user',
            email='sample@sample.com',
            password='testpass1234')
        self.goal = MonthlyGoalFactory(custom_user=self.user1.id)

    def test_user(self):
        self.assertTrue(self.goal)

    def test_user_fail_blank_goal(self):
        with self.assertRaises(IntegrityError):
            MonthlyGoalFactory(username='test_user')
