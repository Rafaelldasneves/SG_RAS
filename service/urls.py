from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [   
    path('list/', views.ServiceListView.as_view(), name="list_services"),
    path('create/', views.ServiceCreateView.as_view(), name="create_service"),
    path('<int:pk>/update/', views.ServiceUpdateView.as_view(), name="update_service"),
    path('<int:pk>/delete/', views.ServiceDeleteView.as_view(), name="delete_service"),
]