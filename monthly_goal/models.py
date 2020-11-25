from django.db import models
from account.models import CustomUser
import datetime
# Create your models here.
date_string = datetime.datetime.now()
category_choice = (
    ('', '選択肢から選んでください'),
    ('0', '健康'),
    ('1', 'ビジネス'),
    ('2', '学習'),
    ('3', '家事'),
    ('4', 'プライベート'),
    ('5', 'アウトドア・旅行'),
    ('6', 'その他'),
)

score_choice = (
    ('', '自己評価'),
    ('0', 1),
    ('1', 2),
    ('2', 3),
    ('3', 4),
    ('4', 5),
)


class MonthlyGoal(models.Model):
    class Meta:
        db_table = 'monthly_goal'

    custom_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    year = models.IntegerField(verbose_name='目標期限（年）', default=date_string.year)
    month = models.IntegerField(verbose_name='目標期限（月末）', default=date_string.month)
    category = models.CharField(
        verbose_name='カテゴリー', choices=category_choice, max_length=255, null=True, blank=True)
    goal = models.CharField(verbose_name='達成目標', help_text='1〜数ヶ月で達成したい目標', max_length=255)
    why_need_goal = models.TextField(
        verbose_name='目標設定動機', help_text='なぜその目標を達成したいのか？（未設定可）',
        max_length=255, null=True, blank=True)
    score = models.IntegerField(
        verbose_name='自己評価', choices=score_choice, null=True,
        help_text='目標達成及び期限が来たら入力', blank=True)
    revised_goal = models.CharField(
        verbose_name='修正目標', max_length=255, null=True, blank=True)
    why_revise = models.TextField(
        verbose_name='目標修正理由',
        max_length=255, null=True,
        help_text='なぜ目標を修正するのか？（未設定可）', blank=True)
