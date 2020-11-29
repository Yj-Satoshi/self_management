from django import forms
from .models import MonthlyGoal


class GoalScoreForm(forms.ModelForm):
    score = forms.IntegerField(
        required=False,
        label='自己評価')

    after_memo = forms.TextField(
        required=False,
        verbose_name='後書きメモ',
        max_length=500, null=True,
        help_text='評価の際の反省点などの後から振り返るメモ（未設定可）', blank=True)

    def clean_age(self):
        score = self.cleaned_data.get('score')
        if score < 1 or score > 5:
            raise forms.ValidationError('1〜5のみです!')
        return score

    class Meta():
        model = MonthlyGoal
        fields = (
             'socore', 'after_memo'
        )
