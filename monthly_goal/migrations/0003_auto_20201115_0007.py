# Generated by Django 3.1.2 on 2020-11-14 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monthly_goal', '0002_auto_20201113_0038'),
    ]

    operations = [
        migrations.RenameField(
            model_name='monthlygoal',
            old_name='custom_user_id',
            new_name='custom_user',
        ),
    ]
