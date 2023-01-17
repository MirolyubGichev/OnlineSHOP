from django.contrib.auth import forms, get_user_model, login
from django import forms as djangoForms
from django.contrib.auth.forms import PasswordChangeForm

from Online_shop.accounts.models import User_profile, User_address

User_model = get_user_model()


class UserRegisterForm(forms.UserCreationForm):

    class Meta:
        model = User_model
        fields = ['username', 'password1', 'password2']
        widgets = {
            'username':djangoForms.TextInput(
                attrs= {'class' : 'form-control'}
            )
        }

    password1 = djangoForms.CharField(widget=djangoForms.PasswordInput(attrs={'placeholder': 'Password',
                                                                              'class': 'form-control',
                                                                              }),
                                      label='Password')
    password2 = djangoForms.CharField(widget=djangoForms.PasswordInput(attrs={'placeholder': 'Confirm Password',
                                                                              'class': 'form-control',

                                                                              }),
                                      label='Re-Password')


class UserProfileForm(djangoForms.ModelForm):
    def __init__(self,user,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.user = user

    def save(self, commit=True):
        u =super().save(commit=False)
        u.user = self.user
        if commit :
            u.save()
        return u

    class Meta:
        model= User_profile
        exclude = ["user"]
        widgets = {
            'user_first_name' : djangoForms.TextInput(attrs={'class' : 'form-control'}),
            'user_last_name' : djangoForms.TextInput(attrs={'class' : 'form-control'}),
            'user_email' : djangoForms.TextInput(attrs={'class' : 'form-control'}),
            'user_phone' : djangoForms.TextInput(attrs={'class' : 'form-control'}),

        }


class UserAddressForm(djangoForms.ModelForm):
    def __init__(self,user_profile,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.user_profile = user_profile

    def save(self, commit=True):
        u =super().save(commit=False)
        u.user_profile = self.user_profile
        if commit :
            u.save()
        return u

    class Meta:
        model= User_address
        exclude = ['user_profile']
        widgets = {
            'country' : djangoForms.TextInput(attrs={'class' : 'form-control'}),
            'city' : djangoForms.TextInput(attrs={'class' : 'form-control'}),
            'address' : djangoForms.TextInput(attrs={'class' : 'form-control'}),
            'additional_info' : djangoForms.TextInput(attrs={'class' : 'form-control'}),
        }


class UserPasswordChageForm(PasswordChangeForm):
    def __init__(self, user, *args, **kwargs):
        self.user = user
        super().__init__(user, *args, **kwargs)
        self.fields['old_password'].widget.attrs.update({'class': 'form-control', 'placeholder': "Old Password"})
        self.fields['new_password1'].widget.attrs.update({'class': 'form-control', 'placeholder': "New Password"})
        self.fields['new_password2'].widget.attrs.update({'class': 'form-control', 'placeholder': "New Password"})

    def save(self, commit=True):
        password = self.cleaned_data["new_password1"]
        self.user.set_password(password)
        if commit:
            self.user.save()
        return self.user