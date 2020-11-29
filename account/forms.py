from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
gender_choice = (
    ('0', '未設定'),
    ('1', '男性'),
    ('2', '女性'),
)

address_choice = (
    ('301', '宗谷地方'),
    ('302', '上川・留萌地方'),
    ('303', '網走・北見・紋別地方'),
    ('304', '釧路・根室・十勝地方'),
    ('305', '胆振・日高地方'),
    ('306', '石狩・空知・後志地方'),
    ('307', '渡島・檜山地方'),
    ('308', '青森県'),
    ('309', '秋田県'),
    ('310', '岩手県'),
    ('311', '山形県'),
    ('312', '宮城県'),
    ('313', '福島県'),
    ('314', '茨城県'),
    ('315', '群馬県'),
    ('316', '栃木県'),
    ('317', '埼玉県'),
    ('318', '千葉県'),
    ('319', '東京都'),
    ('320', '神奈川県'),
    ('321', '山梨県'),
    ('322', '長野県'),
    ('323', '新潟県'),
    ('324', '富山県'),
    ('325', '石川県'),
    ('326', '福井県'),
    ('327', '静岡県'),
    ('328', '岐阜県'),
    ('329', '愛知県'),
    ('330', '三重県'),
    ('331', '大阪府'),
    ('332', '兵庫県'),
    ('333', '京都府'),
    ('334', '滋賀県'),
    ('335', '奈良県'),
    ('336', '和歌山県'),
    ('337', '島根県'),
    ('338', '広島県'),
    ('339', '鳥取県'),
    ('340', '岡山県'),
    ('341', '香川県'),
    ('342', '愛媛県'),
    ('343', '徳島県'),
    ('344', '高知県'),
    ('345', '山口県'),
    ('346', '福岡県'),
    ('347', '佐賀県'),
    ('348', '長崎県'),
    ('349', '熊本県'),
    ('350', '大分県'),
    ('351', '宮崎県'),
    ('352', '鹿児島県'),
    ('353', '沖縄本島地方'),
    ('354', '大東島地方'),
    ('355', '宮古島地方'),
    ('356', '八重山地方'),
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
    address = forms.ChoiceField(
        label='住所', initial=319, choices=address_choice)

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email', 'birth_year', 'gender', 'address', 'profession')


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


class UserUpdateForm(forms.ModelForm):
    birth_year = forms.IntegerField(
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
    address = forms.ChoiceField(
        label='住所', required=False, choices=address_choice)

    class Meta:
        model = CustomUser
        fields = ('email', 'birth_year', 'address', 'gender', 'profession')
