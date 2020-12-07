from django.contrib.auth import get_user_model
from factory.django import DjangoModelFactory
from factory.fuzzy import FuzzyInteger, FuzzyText
from factory import Faker
from factory import Sequence

# from .. models import CustomUser

CustomUserModel = get_user_model()
FAKER_LOCALE = 'ja_JP'


class CustomUserFactory(DjangoModelFactory):

    class Meta:
        model = CustomUserModel

    username = Sequence(lambda n: 'user{0}'.format(n))
    password = FuzzyText(length=12, suffix='192837')
    email = FuzzyText(length=12, suffix='@example.com')
    birth_year = FuzzyInteger(low=0, high=9999)
    gender = FuzzyInteger(low=1, high=2)
    address = FuzzyInteger(low=301, high=356)
    profession = Faker('text', max_nb_chars=30, locale=FAKER_LOCALE)
