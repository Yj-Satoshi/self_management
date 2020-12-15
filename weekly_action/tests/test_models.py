from django.test import TestCase
from django.db.utils import IntegrityError

from .factory import CustomUserFactory
from .factory import MonthlyGoalFactory
from .factory import WeeklyActionFactory


class MonthlyGoalTests(TestCase):
    def setUp(self):
        self.user1 = CustomUserFactory()
        self.goal = MonthlyGoalFactory()
        self.action = WeeklyActionFactory()

    def test_action(self):
        self.assertTrue(self.action)

    def test_user_fail_blank_user(self):
        with self.assertRaises(IntegrityError):
            WeeklyActionFactory(custom_user=None)

    def test_user_fail_blank_action(self):
        with self.assertRaises(TypeError):
            WeeklyActionFactory(weekly_action=None)

    def test_user_fail_blank_week_no(self):
        with self.assertRaises(IntegrityError):
            WeeklyActionFactory(week_no=None)

    def test_user_fail_wrong_score(self):
        self.action1 = WeeklyActionFactory(score=-1).save()
        self.assertFalse(self.action1)
