from django.contrib.auth import forms, get_user_model, login
from django import forms as djangoForms

from Online_shop.accounts.models import User_profile

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
        print(u)
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
