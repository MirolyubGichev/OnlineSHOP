from django.contrib.auth import login, update_session_auth_hash ,views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
import django.views.generic as generic_views


from Online_shop.accounts.forms import UserRegisterForm, UserProfileForm, UserAddressForm, UserPasswordChageForm
from Online_shop.accounts.models import User_profile, User_address


class UserRegisterView(generic_views.CreateView):
    form_class = UserRegisterForm
    template_name = "accounts/profile_register.html"
    success_url = reverse_lazy("profile register")




    def form_valid(self, *args, **kwargs):
        result = super().form_valid(*args, **kwargs)

        login(self.request, self.object)
        return result
    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()


class UserProfileRegisterView(LoginRequiredMixin,generic_views.CreateView):

    form_class = UserProfileForm
    template_name = 'accounts/user_register.html'
    success_url = reverse_lazy('address register')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()


class UserAddressRegisterView(LoginRequiredMixin,generic_views.CreateView):
    form_class = UserAddressForm
    template_name = 'accounts/address_register.html'
    success_url = reverse_lazy('Index')



    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        user_profile = User_profile.objects.get(pk= self.request.user.pk)
        kwargs['user_profile'] = user_profile
        return kwargs

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()
    pass


class UserPasswordEditView(LoginRequiredMixin,generic_views.TemplateView):

    form_class = UserPasswordChageForm

    def get(self, request, *args, **kwargs):

        form = self.form_class(self.request.user)
        return render(request, 'accounts/password_change.html',{'form': form,})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            return render(request, 'Index.html', {'form': form, 'password_changed': True})
        else:
            return render(request, 'accounts/password_change.html', {'form': form, 'password_changed': False})


class UserProfileEditView(LoginRequiredMixin,generic_views.UpdateView,SuccessMessageMixin,):
    login_url = reverse_lazy()

    model = User_profile
    template_name  = 'accounts/profile_edit.html'
    success_url = reverse_lazy('Index')
    fields = ['user_first_name','user_last_name','user_email','user_phone']
    success_message = 'Information successfully updated'

    def put(self, *args, **kwargs):
        kwargs = super().get_form_kwargs()
        return self.post(kwargs)


class UserAddressEditView(LoginRequiredMixin,generic_views.UpdateView,SuccessMessageMixin,):
    login_url = reverse_lazy()

    model = User_address
    template_name  = 'accounts/address_edit.html'
    success_url = reverse_lazy('Index')
    fields = ['country','city','address','additional_info']
    success_message = 'Information successfully updated'

    def put(self, *args, **kwargs):
        kwargs = super().get_form_kwargs()
        return self.post(kwargs)


class UserLogOutView(views.LogoutView):
    next_page = reverse_lazy('Index')


class UserAddressDeleteView(LoginRequiredMixin,generic_views.DeleteView):
    login_url = reverse_lazy('Index')

    model = User_address
    success_url = reverse_lazy('user details')
    template_name = 'accounts/addres_delete.htlm.html'


class UserLoginView(views.LoginView):
    template_name = 'accounts/user_login.html'
    success_url = reverse_lazy('Index')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()


class ProfileDetails(LoginRequiredMixin,generic_views.TemplateView):

    template_name = 'accounts/profile_details.html'

    def get(self, request, *args, **kwargs):
        addresses = User_address.objects.all().filter(user_profile=request.user.pk)
        return  render(request,'accounts/profile_details.html' ,{'addresses': addresses})
