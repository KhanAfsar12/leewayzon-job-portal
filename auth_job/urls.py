from django.urls import path
from . import views


urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('jobs/', views.jobsView, name='jobs'),
    path('description/<int:job_id>/', views.description, name='description'),
    path('application/', views.application_view, name='application'),
    path('user_data/<int:user_id>/', views.UserDataView, name='user_data'),
    path('ag-grid-applications/', views.ag_grid_view, name='ag_grid_applications'),
    path('api/applications/', views.application_data, name='application_data'),
]