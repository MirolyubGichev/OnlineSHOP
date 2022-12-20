from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Online_shop.web.urls'),),
    path('acc/', include('Online_shop.accounts.urls')),

]
