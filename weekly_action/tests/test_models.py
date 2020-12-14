from django.test import TestCase
# from django.db.utils import IntegrityError

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

    # def test_user_fail_blank_user(self):
    #     with self.assertRaises(IntegrityError):
    #         MonthlyGoalFactory(custom_user=None)

    # def test_user_fail_blank_goal(self):
    #     with self.assertRaises(TypeError):
    #         MonthlyGoalFactory(monthly_goal=None)

    # def test_user_fail_blank_year(self):
    #     with self.assertRaises(IntegrityError):
    #         MonthlyGoalFactory(year=None)

    # def test_user_fail_blank_month(self):
    #     with self.assertRaises(IntegrityError):
    #         MonthlyGoalFactory(month=None)

    # def test_user_fail_wrong_month(self):
    #     self.goal1 = MonthlyGoalFactory(month=-1).save()
    #     self.assertFalse(self.goal1)

    # def test_user_fail_wrong_score(self):
    #     self.goal1 = MonthlyGoalFactory(score=-1)
    #     self.assertFalse(self.goal1)
