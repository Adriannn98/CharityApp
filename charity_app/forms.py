from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


def validate_password(value):
    if len(value) < 8:
        raise ValidationError("Password is too short")


def check_if_has_number(value):
    if not any(x for x in value if x.isdigit()):
        raise ValidationError("Password must have a number")

class RegisterForm(forms.ModelForm):
    password1 = forms.CharField(label='Password',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}),
                                validators=[validate_password, check_if_has_number],
                                help_text='Password must have min. 8 charactrs')
    password2 = forms.CharField(label='re-Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

    def clean(self):
        data = super().clean()
        pass1 = data.get('password1')
        if pass1 is not None and pass1 != data.get('password2'):
            raise ValidationError('Hasła nie są identyczne')
        return data


class LoginForm(forms.Form):
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'Email',
                                                           'class': 'form-group'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'password', 'class': 'form-group'}),
                               required=False)