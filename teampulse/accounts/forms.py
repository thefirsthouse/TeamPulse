from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'id': 'id_username', 'required': True})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'id': 'id_password', 'required': True})
    )
