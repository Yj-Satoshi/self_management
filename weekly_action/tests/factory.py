import factory
from django.contrib.auth import get_user_model
from factory.django import DjangoModelFactory
from factory.fuzzy import FuzzyInteger, FuzzyText
from factory import Faker
from factory import Sequence

from monthly_goal.models import MonthlyGoal
from .. models import WeeklyAction
CustomUser = get_user_model()

FAKER_LOCALE = 'ja_JP'


class CustomUserFactory(DjangoModelFactory):
    class Meta:
        model = CustomUser

    username = Sequence(lambda n: 'user{0}'.format(n))
    password = FuzzyText(length=12, suffix='192837')
    email = FuzzyText(length=12, suffix='@example.com')
    birth_year = FuzzyInteger(low=0, high=9999)
    gender = FuzzyInteger(low=1, high=2)
    address = FuzzyInteger(low=301, high=356)
    profession = Faker('text', max_nb_chars=30, locale=FAKER_LOCALE)


class MonthlyGoalFactory(DjangoModelFactory):
    class Meta:
        model = MonthlyGoal

    custom_user = factory.SubFactory(CustomUserFactory)
    year = FuzzyInteger(low=0, high=9999)
    month = FuzzyInteger(low=1, high=12)
    category = FuzzyInteger(low=1, high=6)
    score = FuzzyInteger(low=1, high=5)
    goal = Faker('text', max_nb_chars=255, locale=FAKER_LOCALE)
    why_need_goal = Faker('text', max_nb_chars=500, locale=FAKER_LOCALE)
    revised_goal = Faker('text', max_nb_chars=255, locale=FAKER_LOCALE)
    why_revise = Faker('text', max_nb_chars=500, locale=FAKER_LOCALE)
    after_memo = Faker('text', max_nb_chars=500, locale=FAKER_LOCALE)


class WeeklyActionFactory(DjangoModelFactory):
    class Meta:
        model = WeeklyAction

    custom_user = factory.SubFactory(CustomUserFactory)
    monthly_goal = factory.SubFactory(MonthlyGoalFactory)
    year = FuzzyInteger(low=0, high=9999)
    week_no = FuzzyInteger(low=1, high=12)
    score = FuzzyInteger(low=1, high=5)
    goal_action = Faker('text', max_nb_chars=255, locale=FAKER_LOCALE)
    why_select_action = Faker('text', max_nb_chars=500, locale=FAKER_LOCALE)
    after_memo = Faker('text', max_nb_chars=500, locale=FAKER_LOCALE)
