from factory.django import DjangoModelFactory
from factory.fuzzy import FuzzyInteger, FuzzyText
from factory import Sequence

from . models import CustomUser
from myapp.utils.datetime import get_good_old_time

_default_start_dt = get_good_old_time()


class CustomUserFactory(DjangoModelFactory):

    class Meta:
        model = CustomUser

    username = Sequence(lambda n: 'user{0}'.format(n))
    password = 
    email = FuzzyText(length=12, suffix='@example.com')
    birth_year = FuzzyInteger(low=0, high=99999)
    gender = FuzzyInteger(low=1, high=2)
    address = FuzzyInteger(low=301, high=356)
    profession = FuzzyText()
