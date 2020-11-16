from django import forms
from .models import MonthlyGoal
# from .models import CustomUser

category_choice = (
    ('', '選択肢から選んでください'),
    ('0', '健康'),
    ('1', 'ビジネス'),
    ('2', 'IT'),
    ('3', '家事'),
    ('4', 'プライベート'),
    ('5', 'その他'),
)


# class CreateGoalForm(forms.ModelForm):
#     year = forms.IntegerField(
#         required=False,
#         label='目標期限（年）')
#     month = forms.IntegerField(
#         required=False,
#         label='目標期限（月末）')
#     category = forms.ChoiceField(
#         widget=forms.Select, choices=category_choice,
#         required=False,
#         label='カテゴリー')
#     goal = forms.CharField(
#         required=False,
#         help_text='1〜数ヶ月で達成したい目標',
#         label='目標')
#     why_need_goal = forms.CharField(
#         required=False,
#         help_text='なぜその目標を達成したいのか？（未設定可）',
#         label='目標設定動機')
#     # custom_user = forms.IntegerField()

#     class Meta:
#         model = MonthlyGoal
#         fields = (
#             'year', 'month', 'category', 'goal', 'why_need_goal',
#         )


class UpdateGoalForm(forms.Form):
    sccore = forms.IntegerField(
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
