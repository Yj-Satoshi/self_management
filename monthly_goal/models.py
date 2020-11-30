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
    goal = models.CharField(verbose_name='達成目標', help_text='1月単位で達成したい目標', max_length=255)
    why_need_goal = models.TextField(
        verbose_name='目標設定動機', help_text='なぜその目標を達成したいのか？プラン設定("P")の確認（未設定可）',
        max_length=500, null=True, blank=True)
    score = models.IntegerField(
        verbose_name='自己評価', validators=[clean_score], null=True,
        help_text='目標達成及び期限が来たら入力。達成度チェック("C")（範囲１〜５, 数字が高い程、評価良）', blank=True)
    revised_goal = models.CharField(
        verbose_name='修正目標', max_length=255, null=True, blank=True)
    why_revise = models.TextField(
        verbose_name='目標修正理由',
        max_length=500, null=True,
        help_text='目標を修正する理由。最初の目標のプラン設定("P")は妥当であったか確認（未設定可）', blank=True)
    after_memo = models.TextField(
        verbose_name='後書きメモ',
        max_length=500, null=True,
        help_text='反省点などの振り返りメモ。達成度チェック("C")・次の目標("A")の確認（未設定可）', blank=True)
