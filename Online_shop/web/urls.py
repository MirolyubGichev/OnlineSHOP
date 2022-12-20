from django.urls import path
from Online_shop.web.views import Index


urlpatterns = (
    path('', Index.as_view() , name = 'Index'),
)