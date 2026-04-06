from django.contrib import admin
from django.urls import path, include
from accounts import views
from periods import views
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home.as_view(), name="home"),
    path('accounts/', include('accounts.urls')),
    path('periods/', include('periods.urls')),
    path('service/', include('service.urls')),
]
