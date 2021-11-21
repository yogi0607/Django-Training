from django.contrib import admin
from django.urls import path, include
from . import views
from .views import *


urlpatterns = [
    path('', views.IndexView.as_view(), name='indexview'),
    path('opentickets', views.OpenTicketView.as_view(), name='opentickets'),
    path('acceptedtickets', views.AcceptedTicketView.as_view(), name='acceptedtickets'),
    path('createtickets', views.CreateTicketView.as_view(), name='createtickets'),
    path('updateticket/<str:pk>', views.UpdateTicketView.as_view(), name='updateticket'),
    path('completedtickets', views.CompletedTicketView.as_view(), name='completedtickets'),
    path('closedtickets', views.ClosedTicketView.as_view(), name='closedtickets'),
    path('alltickets', views.AllTicketView.as_view(), name='alltickets'),

    path('pmlogin', views.loginmanager, name='pmlogin'),
    path('pmlogout', views.logoutmanager, name='pmlogout'),
  
    path('pmsignup', views.signupmanager, name='pmsignup'),
    path('pmdashboard', views.pmdashboard, name='pmdashboard'),

    path('devlogin', views.logindeveloper, name='devlogin'),

    path('dev_opentickets', views.DevOpenTicketView.as_view(), name='dev_opentickets'),
    path('dev_acceptedtickets', views.DevAcceptedTicketView.as_view(), name='dev_acceptedtickets'),
    path('dev_updateticket/<str:pk>', views.DevUpdateTicketView.as_view(), name='dev_updateticket'),
    path('dev_closedtickets', views.DevClosedTicketView.as_view(), name='dev_closedtickets'),
    path('dev_completedtickets', views.DevCompletedTicketView.as_view(), name='dev_completedtickets'),

    path('devlogout', views.logoutdevloper, name='devlogout'),
    path('devsignup', views.signupdeveloper, name='devsignup'),
    path('devdashboard', views.devdashboard, name='devdashboard'),

    
]