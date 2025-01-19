from . import views
from django.urls import path
urlpatterns = [
    path('', views.service_request_list, name='service_request_list'),
    path('create/', views.service_request_create, name='service_request_create'),
    path('<int:request_id>/edit/', views.service_request_edit, name='service_request_edit'),
    path('<int:request_id>/delete/', views.service_request_delete, name='service_request_delete'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('login/',views.login_view,name='login'),
    path('agent/', views.agent_dashboard, name='agent_dashboard'),
    path('agent/<int:request_id>/', views.agent_request_detail, name='agent_request_detail'),
]
