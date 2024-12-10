from django import forms
from django.contrib.auth.models import User
from .models import Profile

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={
        'placeholder': 'Username',
        'class': 'form-control'
    }), label="Username")
    
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Password',
        'class': 'form-control'
    }), label="Password")

    role = forms.ChoiceField(choices=Profile.USER_ROLES, label="Role", required=True)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        role = cleaned_data.get('role')

        try:
            user = User.objects.get(username=username)
            profile = Profile.objects.get(user=user)
            
            if profile.role != role:
                raise forms.ValidationError(f"Role mismatch. User is not registered as {role}.")
        except User.DoesNotExist:
            raise forms.ValidationError("No such user exists.")
        except Profile.DoesNotExist:
            raise forms.ValidationError("Profile not found for this user.")
        
        return cleaned_data


class RegisterForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput, label="Password")
    password2 = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")
    role = forms.ChoiceField(choices=Profile.USER_ROLES, label="Role", required=True)

    class Meta:
        model = User
        fields = ['username', 'email']

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 != password2:
            raise forms.ValidationError("Passwords do not match.")
        return password2
