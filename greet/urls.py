from django.contrib import admin
from django.urls import path, include
from . import views
from .views import *


app_name = 'tickets'

urlpatterns = [
    path('', views.IndexView.as_view(), name='indexview'),
    path('opentickets', views.OpenTicketView.as_view(), name='opentickets'),
    path('acceptedtickets', views.AcceptedTicketView.as_view(), name='acceptedtickets'),
    path('createtickets', views.CreateTicketView.as_view(), name='createtickets'),

    path('pmlogin', views.loginmanager, name='pmlogin'),
    path('pmlogout', views.logoutmanager, name='pmlogout'),
  
    path('pmsignup', views.signupmanager, name='pmsignup'),
    path('pmdashboard', views.pmdashboard, name='pmdashboard'),
    path('ticketform', views.createTicket, name='ticketform'),
    path('viewticket', views.viewTickets, name='viewticket'),
    path('updatepm/<str:pk>', views.updatepm, name='updatepm'),
    # path('pm_open_tickets', views.pm_openTickets, name='pm_open_tickets'),
    # path('pm_accepted_tickets', views.pm_acceptedTickets, name='pm_accepted_tickets'),
    path('pm_completed_tickets', views.pm_completedTickets, name='pm_completed_tickets'),
    path('pm_closed_tickets', views.pm_closedTickets, name='pm_closed_tickets'),
    # path('pm_get_tickets', views.pm_getTickets, name='pm_get_tickets'),
    path('devlogin', views.logindeveloper, name='devlogin'),
    path('opentickets', views.openTickets, name='opentickets'),
    path('acceptedticket', views.acceptedTickets, name='acceptedticket'),
    path('completedticket', views.completedTickets, name='completedticket'),
    path('closedticket', views.closedTickets, name='closedticket'),
    # path('getticket', views.getTickets, name='getticket'),
    path('updatedev/<str:pk>', views.updatedev, name='updatedev'),
    path('devlogout', views.logoutdevloper, name='devlogout'),
    path('devsignup', views.signupdeveloper, name='devsignup'),
    path('devdashboard', views.devdashboard, name='devdashboard'),

    
]