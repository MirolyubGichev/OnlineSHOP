from django.urls import path

from Online_shop.accounts.views import UserRegisterView, UserProfileCreateView

urlpatterns = (
    path('register/',UserRegisterView.as_view() , name = "register"),
    path('setprofile/',UserProfileCreateView.as_view() , name = "profile"),

)