from django.contrib import admin
from django.urls import path, include
from accounts import views
from . import views

urlpatterns = [
    path("__reload__/", include("django_browser_reload.urls")),
    path('admin/', admin.site.urls),
    path('', views.Home.as_view(), name="home"),
    path('accounts/', include('accounts.urls')),
]
