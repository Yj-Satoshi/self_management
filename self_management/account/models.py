from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    class Meta:
        db_table = 'custom_user'

    birth_year = models.IntegerField(verbose_name='生年(西暦)', null=True, blank=True)
    gender = models.CharField(verbose_name='性別', max_length=5, null=True, blank=True)
    profession = models.CharField(verbose_name='職業', max_length=15, null=True, blank=True)
    address = models.CharField(verbose_name='住所', max_length=15, null=True, blank=True)
