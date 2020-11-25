from django.db import models
from monthly_goal.models import MonthlyGoal
from account.models import CustomUser
import datetime
date_string = datetime.datetime.now()
this_week = round(date_string.day / 7) + 1
# Create your models here.
score_choice = (
    ('', '自己評価'),
    ('0', 1),
    ('1', 2),
    ('2', 3),
    ('3', 4),
    ('4', 5),
)


class WeeklyAction(models.Model):
    class Meta:
        db_table = 'weekly_action'

    monthly_goal = models.ForeignKey(MonthlyGoal, on_delete=models.CASCADE, to_field='id')
    custom_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    week_no = models.IntegerField(verbose_name='週No.', default=this_week)
    goal_action = models.CharField(
        verbose_name='目標達成の為のアクション', help_text='1〜数週で実践する行動', max_length=255)
    why_need_goal = models.TextField(
        verbose_name='アクション設定理由', help_text='なぜそのアクションで目標が達成できるのか？（未設定可）',
        max_length=255, null=True, blank=True)
    score = models.IntegerField(
        verbose_name='自己評価', null=True,
        help_text='アクションを終えたら入力', choices=score_choice, blank=True)
