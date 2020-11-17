from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
gender_choice = (
    ('0', '未設定'),
    ('1', '男性'),
    ('2', '女性'),
)


class SignUpForm(UserCreationForm):
    birth_year = forms.IntegerField(
        initial=1990,
        required=False,
        help_text='未設定可',
        label='生年')
    gender = forms.ChoiceField(
        required=False,
        choices=gender_choice,
        label='性別')
    profession = forms.CharField(
        required=False,
        help_text='未設定可',
        label='職業')

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email', 'birth_year', 'gender', 'profession')


class SignInForm(forms.Form):
    username = forms.CharField(
        label='ユーザー名',
        max_length=255,
    )

    password = forms.CharField(
        label='パスワード',
        strip=False,
        widget=forms.PasswordInput(render_value=True),
    )
