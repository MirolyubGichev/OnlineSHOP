from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
import django.views.generic as generic_views
# Create your views here.
from django.urls import reverse_lazy

from Online_shop.accounts.forms import UserRegisterForm, UserProfileForm


class UserRegisterView(generic_views.CreateView):
    form_class = UserRegisterForm
    template_name = "accounts/profile_register.html"
    success_url = reverse_lazy("profile")




    def form_valid(self, *args, **kwargs):
        result = super().form_valid(*args, **kwargs)

        login(self.request, self.object)
        return result
    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()



class UserProfileCreateView(LoginRequiredMixin,generic_views.CreateView):

    form_class = UserProfileForm
    template_name = 'accounts/user_register.html'
    success_url = reverse_lazy('Index')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()