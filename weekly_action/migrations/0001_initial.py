# Generated by Django 3.1.2 on 2020-11-21 16:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('monthly_goal', '0006_auto_20201122_0128'),
    ]

    operations = [
        migrations.CreateModel(
            name='WeeklyAction',
            fields=[
                ('id', models.AutoField(
                    auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week_no', models.IntegerField(default=4.142857142857142, verbose_name='週No.')),
                ('goal_action', models.CharField(
                    help_text='1〜数週で実践する行動', max_length=255, verbose_name='目標達成の為のアクション')),
                ('why_need_goal', models.TextField(
                    blank=True, help_text='なぜそのアクションで目標が達成できるのか？（未設定可）',
                    max_length=255, null=True, verbose_name='アクション設定理由')),
                ('score', models.IntegerField(
                    blank=True, help_text='アクションを終えたら入力', null=True, verbose_name='自己評価')),
                ('custom_user', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('monthly_goal', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='monthly_goal.monthlygoal')),
            ],
            options={
                'db_table': 'weekly_action',
            },
        ),
    ]
