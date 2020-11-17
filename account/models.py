from django.db import models
from django.contrib.auth.models import AbstractUser

gender_choice = (
    ('', '選択肢から選んでください'),
    ('0', '健康'),
    ('1', 'ビジネス'),
    ('2', 'IT'),
    ('3', '家事'),
    ('4', 'プライベート'),
    ('5', 'その他'),
)


class CustomUser(AbstractUser):
    class Meta:
        db_table = 'custom_user'

    birth_year = models.IntegerField(verbose_name='生年(西暦)', null=True, blank=True)
    gender = models.CharField(verbose_name='性別', max_length=5, null=True, blank=True)
    profession = models.CharField(verbose_name='職業', max_length=15, null=True, blank=True)
