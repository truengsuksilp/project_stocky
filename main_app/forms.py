from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    # Call method on form itself
    def clean(self):
        cleaned_data = super().clean()
        # Add validation of custom fields: see crispy-signup

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )

class LoginForm(User):
    pass

#     class Meta:
#         model = User
#         fields = ('username', 'password1')
    
    