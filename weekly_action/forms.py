from django import forms
from .models import WeeklyAction


class ActionScoreForm(forms.Form):
    score = forms.IntegerField(
        required=False,
        label='自己評価')

    def clean_age(self):
        score = self.cleaned_data.get('score')
        if score < 1 or score > 5:
            raise forms.ValidationError('1〜5のみです!')
        return score

    class Meta():
        model = WeeklyAction
        fields = (
             'socore',
        )
