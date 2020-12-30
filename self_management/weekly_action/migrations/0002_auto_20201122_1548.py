# Generated by Django 3.1.2 on 2020-11-22 06:48

import account.views
from django.db import migrations, models
import django.db.models.deletion
import django.views.generic.edit


class Migration(migrations.Migration):

    dependencies = [
        ('monthly_goal', '0007_auto_20201122_1548'),
        ('weekly_action', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WeeklyActionCreateView',
            fields=[
                ('monthlygoal_ptr', models.OneToOneField(
                    auto_created=True, on_delete=django.db.models.deletion.CASCADE,
                    parent_link=True, primary_key=True, serialize=False,
                    to='monthly_goal.monthlygoal')),
            ],
            bases=(
                django.views.generic.edit.CreateView,
                account.views.MyPageView, 'monthly_goal.monthlygoal'),
        ),
        migrations.RenameField(
            model_name='weeklyaction',
            old_name='score',
            new_name='score',
        ),
        migrations.AlterField(
            model_name='weeklyaction',
            name='week_no',
            field=models.IntegerField(default=4, verbose_name='週No.'),
        ),
    ]