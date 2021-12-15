from django.contrib import admin
from django.urls import path, include
from . import views
from .views import *


urlpatterns = [
    path('', views.IndexView.as_view(), name='indexview'),
    path('login_success', views.login_success, name='login_success'),
    path('createtickets', views.CreateTicketView.as_view(), name='createtickets'),
    path('updateticket/<str:pk>', views.UpdateTicketView.as_view(), name='updateticket'),
    path('alltickets/<slug:status>', views.AllTicketView.as_view(), name='alltickets'),

    path('pmlogin', views.loginmanager, name='pmlogin'),
    path('pmlogout', views.logoutmanager, name='pmlogout'),
  
    # path('pmsignup', views.signupmanager, name='pmsignup'),
    path('pmsignup', views.RegisterManager.as_view(), name='pmsignup'),
    path('pmdashboard', views.DashboardView.as_view(), name='pmdashboard'),


    path('devdashboard', views.DevDashboardView.as_view(), name='devdashboard'),
    # path('devlogin', views.logindeveloper, name='devlogin'),
    path('devlogin', views.DeveloperLoginView.as_view(), name='devlogin'),

    path('devlogout', views.logoutdevloper, name='devlogout'),
    # path('devsignup', views.signupdeveloper, name='devsignup'),
    path('devsignup', views.RegisterDeveloper.as_view(), name='devsignup'),
    # path('devdashboard', views.DevDashboardView.as_view(), name='devdashboard'),
    path('dev-ticket/<slug:status>', views.DevTicketView.as_view(), name='dev-ticket'),
    path('dev_updateticket/<str:pk>', views.DevUpdateTicketView.as_view(), name='dev_updateticket'),


    
]