from django import forms
from django.contrib.auth import (
    authenticate,
    get_user_model
)

User = get_user_model()


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        userID = self.cleaned_data.get('userID')
        password = self.cleaned_data.get('password')

        if userID and password:
            user = authenticate(username=userID, password=password)
            if not user:
                raise forms.ValidationError('This user does not exist')
            if not user.check_password(password):
                raise forms.ValidationError('Incorrect password')
            if not user.is_active:
                raise forms.ValidationError('This user is not active')
        return super(UserLoginForm, self).clean(*args, **kwargs)