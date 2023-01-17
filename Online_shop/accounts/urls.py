from django.urls import path

from Online_shop.accounts.views import UserRegisterView, UserProfileRegisterView, \
    UserAddressRegisterView, UserPasswordEditView, UserProfileEditView, UserAddressEditView, \
    UserAddressDeleteView, UserLoginView, ProfileDetails, UserLogOutView

urlpatterns = (

    path('login/', UserLoginView.as_view(), name = 'user login'),
    path('logout/', UserLogOutView.as_view(), name = 'user logout'),
    path('details/', ProfileDetails.as_view(), name = 'user details'),

    path('register/account/',UserRegisterView.as_view() , name = "account register"),
    path('register/profile/',UserProfileRegisterView.as_view() , name = "profile register"),
    path('register/address/',UserAddressRegisterView.as_view(), name = "address register"),

    path('edit/password/<int:pk>', UserPasswordEditView.as_view(), name='password edit'),
    path('edit/profile/<int:pk>',UserProfileEditView.as_view() , name = "profile edit"),
    path('edit/address/<int:pk>',UserAddressEditView.as_view(), name = "address edit"),

    path('delete/address/<int:pk>',UserAddressDeleteView.as_view(), name = "address delete"),

)