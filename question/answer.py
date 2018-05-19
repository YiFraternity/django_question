from django import forms

class AskQuestion(forms.Form):
    user_answer = forms.CharField(
        required=True,
        label="答案",
        error_messages={'required':'请输入您的答案'},
        widget=forms.Textarea(),
    )



