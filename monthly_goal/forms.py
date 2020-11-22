from django import forms
from .models import MonthlyGoal
# from .models import CustomUser


class UpdateGoalForm(forms.Form):
    score = forms.IntegerField(
        required=False,
        help_text='目標達成及び期限が来たら入力',
        label='自己評価')
    revised_goal = forms.CharField(
        required=False,
        label='修正目標')
    why_revise = forms.CharField(
        required=False,
        help_text='なぜ目標を修正するのか？（未設定可）',
        label='目標修正理由')

    class Meta():
        model = MonthlyGoal
        fields = (
            'why_need_goal', 'soccore', 'revised_goal', 'why_revise'
        )
