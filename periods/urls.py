from django.urls import path
from periods import views

urlpatterns = [
    path('list/', views.PeriodListView.as_view(), name="list_periods"),
    path('create/', views.PeriodCreateView.as_view(), name="create_periods"),
    path('<int:pk>/detail/', views.PeriodDetailView.as_view(), name="detail_period"),
    path('<int:pk>/update/', views.PeriodUpdateView.as_view(), name="update_period"),
    path('<int:pk>/delete/', views.PeriodDeleteView.as_view(), name="delete_period"),    
]
