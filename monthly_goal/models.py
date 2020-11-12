from django.db import models
from account.models import CustomUser
# Create your models here.


class MonthlyGoal(models.Model):
    class Meta:
        db_table = 'monthly_goal'

    custom_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    year = models.IntegerField(verbose_name='year')
    month = models.IntegerField(verbose_name='month')
    category = models.CharField(verbose_name='category', max_length=255, null=True, blank=True)
    goal = models.CharField(verbose_name='goal', max_length=255)
    why_need_goal = models.TextField(
        verbose_name='Why_need_goal',
        max_length=255, null=True, blank=True)
    sccore = models.IntegerField(verbose_name='sccore', null=True, blank=True)
    revised_goal = models.CharField(
        verbose_name='revised_goal', max_length=255, null=True, blank=True)
    why_revise = models.TextField(
        verbose_name='Why_revise',
        max_length=255, null=True, blank=True)
