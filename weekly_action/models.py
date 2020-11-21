from django.db import models
from monthly_goal.models import MonthlyGoal
import datetime
date_string = datetime.datetime.now()
# Create your models here.


class WeeklyAction(models.Model):
    class Meta:
        db_table = 'weekly_action'

    monthly_goal = models.ForeignKey(MonthlyGoal, on_delete=models.CASCADE)
    week_no = models.IntegerField(verbose_name='週No.', default=(date_string.day / 7) + 1)
    goal_action = models.CharField(
        verbose_name='目標達成の為のアクション', help_text='1〜数週で実践する行動', max_length=255)
    why_need_goal = models.TextField(
        verbose_name='アクション設定理由', help_text='なぜそのアクションで目標が達成できるのか？（未設定可）',
        max_length=255, null=True, blank=True)
    sccore = models.IntegerField(
        verbose_name='自己評価', null=True,
        help_text='アクションを終えたら入力', blank=True)
