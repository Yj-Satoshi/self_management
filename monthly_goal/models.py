from django.db import models
from account.models import CustomUser
from django.core.exceptions import ValidationError
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


def clean_score(value):
    if value < 1 or value > 5:
        raise ValidationError('1~5が範囲です')


def clean_month(value):
    if value < 1 or value > 12:
        raise ValidationError('1~12月が範囲です')


class MonthlyGoal(models.Model):
    class Meta:
        db_table = 'monthly_goal'

    custom_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    year = models.IntegerField(verbose_name='目標期限（年）', default=date_string.year)
    month = models.IntegerField(
        verbose_name='目標期限（月末）', validators=[clean_month], default=date_string.month)
    category = models.CharField(
        verbose_name='カテゴリー', choices=category_choice, max_length=255, null=True, blank=True)
    goal = models.CharField(verbose_name='達成目標', help_text='その月で達成したい目標', max_length=255)
    why_need_goal = models.TextField(
        verbose_name='目標設定動機', help_text='なぜその目標を達成したいのか？（未設定可）',
        max_length=500, null=True, blank=True)
    score = models.IntegerField(
        verbose_name='自己評価', validators=[clean_score], null=True,
        help_text='目標達成及び期限が来たら入力（範囲１〜５）', blank=True)
    revised_goal = models.CharField(
        verbose_name='修正目標', max_length=255, null=True, blank=True)
    why_revise = models.TextField(
        verbose_name='目標修正理由',
        max_length=500, null=True,
        help_text='なぜ目標を修正するのか？（未設定可）', blank=True)
    afte_memo = models.TextField(
        verbose_name='後書きメモ',
        max_length=500, null=True,
        help_text='評価の際の反省点などの後から振り返るメモ（未設定可）', blank=True)
