from factory.django import DjangoModelFactory
from factory.fuzzy import FuzzyInteger, FuzzyText
from factory import Sequence

from .models import CustomUser


class CustomUserFactory(DjangoModelFactory):

    class Meta:
        model = CustomUser

    username = Sequence(lambda n: 'user{0}'.format(n))
    password = FuzzyText(length=12, suffix='192837')
    email = FuzzyText(length=12, suffix='@example.com')
    birth_year = FuzzyInteger(low=0, high=9999)
    gender = FuzzyInteger(low=1, high=2)
    address = FuzzyInteger(low=301, high=356)
    profession = FuzzyText(high=15)
