from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'gender', 'mobile_number')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['gender'] = forms.ChoiceField(choices=self.GENDER_CHOICES, widget=forms.RadioSelect(attrs={'class': 'gender-field'}))
        self.fields['mobile_number'] = forms.CharField(max_length=15, required=False, widget=forms.TextInput(attrs={'placeholder': 'Mobile Number', 'class': 'mobile-number-field'}))


    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Username',
        'class': 'username-field',
    }))

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Email', 
        'class': 'email-field'
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Password',
        'class': 'password1-field',
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm password',
        'class': 'password2-field',
    }))

    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect(attrs={
        'class': 'gender-field'
    }))

    mobile_number = forms.CharField(max_length=15, required=False, widget=forms.TextInput(attrs={
        'placeholder': 'Mobile Number',
        'class': 'mobile-number-field'
    }))
    
    
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Username',
        'class': '',
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Password',
        'class': '',
    }))


class UpdateProfileForm(UserChangeForm):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    class Meta:
        model = User
        fields = ['username', 'email', 'gender']

    password = None 

    username = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'placeholder': 'Username',
        'class': 'username-field',
    }))

    email = forms.CharField(required=False, widget=forms.EmailInput(attrs={
        'placeholder': 'Email',
        'class': 'email-field',
    }))

    gender = forms.ChoiceField(required=False, choices=GENDER_CHOICES, widget=forms.RadioSelect(attrs={
        'class': 'gender-field'
    }))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class PasswordChangeForm(PasswordChangeForm):
    class Meta:
        model = User

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['old_password'].widget.attrs.update({'class': 'password-field', 'placeholder': 'Old Password'})
        self.fields['new_password1'].widget.attrs.update({'class': 'password-field', 'placeholder': 'New Password'})
        self.fields['new_password2'].widget.attrs.update({'class': 'password-field', 'placeholder': 'Confirm New Password'})

        self.fields['old_password'].required = False
        self.fields['new_password1'].required = False
        self.fields['new_password2'].required = False