from django.db import models
from monthly_goal.models import MonthlyGoal
from account.models import CustomUser
from django.core.exceptions import ValidationError
import datetime
date_string = datetime.datetime.now()
this_week = round(date_string.day / 7) + 1


def clean_score(value):
    if value < 1 or value > 5:
        raise ValidationError('1~5が範囲です')


class WeeklyAction(models.Model):
    class Meta:
        db_table = 'weekly_action'

    monthly_goal = models.ForeignKey(MonthlyGoal, on_delete=models.CASCADE, to_field='id')
    custom_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    week_no = models.IntegerField(verbose_name='週No.', default=this_week)
    goal_action = models.CharField(
        verbose_name='目標達成の為のアクション', help_text='１週間で実践する行動', max_length=255)
    why_select_action = models.TextField(
        verbose_name='アクション設定理由', help_text='なぜそのアクションで目標が達成できるのか？（未設定可）',
        max_length=500, null=True, blank=True)
    score = models.IntegerField(
        verbose_name='自己評価', null=True,
        help_text='アクションを終えたら入力（範囲１〜５）', validators=[clean_score], blank=True)
    after_memo = models.TextField(
        verbose_name='後書きメモ',
        max_length=500, null=True,
        help_text='評価の際の反省点などの後から振り返るメモ（未設定可）', blank=True)
