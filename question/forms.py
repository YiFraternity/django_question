from django import forms

class LoginForm(forms.Form):
    """
    用户登录表单有两个字段username和password，这两个字段是必填项
    """
    username = forms.CharField(
        required=True,
        label="用户名",
        error_messages={'required':'请输入用户名'},
        widget=forms.TextInput(
            attrs={
                'placeholder':"用户名",
            }
        ),
    )
    password = forms.CharField(
        required=True,
        label="密码",
        error_messages={'required':'请输入密码'},
        widget=forms.PasswordInput(
            attrs={
                'placeholder':"密码",
            }
        ),
    )
    def clean(self):
        if not self.is_valid():
            raise forms.ValidationError("用户名和密码为必填项")
        else:
            cleaned_data = super(LoginForm, self).clean()


class RegisterForm(forms.Form):
    gender = (
        ("male","男"),
        ("female","女"),
    )
    level = (
        ("first" ,"高一"),
        ("second" ,"高二"),
        ("third" ,"高三"),
    )
    """
    用户登录表单有两个字段username和password，这两个字段是必填项
    """
    username = forms.CharField(
        required=True,
        label="用户名",
        error_messages={'required':'请输入用户名'},
        widget=forms.TextInput(
            attrs={
                'placeholder':"用户名",
            }
        ),
    )
    password1 = forms.CharField(
        required=True,
        label="密码",
        error_messages={'required':'请输入密码'},
        widget=forms.PasswordInput(
            attrs={
                'placeholder':"密码",
            }
        ),
    )
    password2 = forms.CharField(
        required=True,
        label="确认密码",
        error_messages={'required':'请确认密码'},
        widget=forms.PasswordInput(
            attrs={
                'placeholder':"确认密码",
            }
        ),
    )
    email = forms.CharField(
        required=True,
        label="邮箱",
        widget=forms.EmailInput(
            attrs={
                'placeholder':'邮箱',
            }
        )
    )
    sex = forms.ChoiceField(label='性别',choices=gender)
    grade = forms.ChoiceField(label='年级',choices=level)
    def clean(self):
        if not self.is_valid():
            raise forms.ValidationError("用户名和密码为必填项")
        else:
            cleaned_data = super(RegisterForm, self).clean()

