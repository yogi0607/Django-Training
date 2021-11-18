from django import forms
from django import contrib
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from greet.models import DevProfile, Ticket
from greet.forms import DeveloperCreationForm, TicketForm

from django.views.generic import View, TemplateView


def logindeveloper(request):
    page = 'devlogin'

    if request.user.is_authenticated:
        return redirect('devdashboard')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = DevProfile.objects.get(username=username)
        except:
            messages.error(request, 'Username does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_developer:
            login(request, user)
            return redirect('devdashboard')
        else:
            messages.error(request, 'Username or password is incorrect')

    return render(request, 'greet/devlogin.html')


def logoutdevloper(request):
    logout(request)
    messages.error(request, 'User was logged out')
    return redirect('devlogin')


def signupdeveloper(request):
    page = 'devsignup'
    form = DeveloperCreationForm()

    if request.user.is_authenticated:
        return redirect('pmdashboard')

    if request.method == 'POST':
        form = DeveloperCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            user.save()

            messages.success(request, 'User account was created!')

            login(request, user)
            return redirect('devdashboard')

        else:
            messages.success(request, 'An error has occured during registration')

    context = {'page': page, 'form': form}
    return render(request, 'greet/devlogin.html', context)

@login_required(login_url='devlogin')
def devdashboard(request):
    return render(request, 'greet/developerdashboard.html')


@login_required(login_url='devlogin')
def openTickets(request):
    page = 'opentickets'
    tickets = Ticket.objects.all()
    open_tickets = tickets.filter(status = 'Open')
    context = {'tickets':tickets, 'open_tickets': open_tickets, 'page':page}
    return render(request, 'greet/openTicket.html', context)

@login_required(login_url='devlogin')
def acceptedTickets(request):
    page = 'acceptedticket'
    tickets = Ticket.objects.all()
    profile = request.user.devprofile
    open_tickets = tickets.filter(status = 'Accepted', accessed_by = profile)
    context = {'tickets':tickets, 'open_tickets': open_tickets, 'page':page}
    return render(request, 'greet/openTicket.html', context)

@login_required(login_url='devlogin')
def completedTickets(request):
    page = 'completedticket'
    tickets = Ticket.objects.all()
    profile = request.user.devprofile
    open_tickets = tickets.filter(status = 'Completed', accessed_by = profile)
    context = {'tickets':tickets, 'open_tickets': open_tickets, 'page':page}
    return render(request, 'greet/openTicket.html', context)

@login_required(login_url='devlogin')
def closedTickets(request):
    page = 'closedticket'
    tickets = Ticket.objects.all()
    profile = request.user.devprofile
    open_tickets = tickets.filter(status = 'Closed', accessed_by = profile)
    context = {'tickets':tickets, 'open_tickets': open_tickets, 'page':page}
    return render(request, 'greet/openTicket.html', context)

@login_required(login_url='devlogin')
def updatedev(request, pk):
    ticket = Ticket.objects.get(id=pk)
    profile = request.user.devprofile
    form1 = TicketForm(instance=ticket)
    if request.method == 'POST':
        form1 = TicketForm(request.POST, instance=ticket)
        if form1.is_valid():
            ticket = form1.save(commit=False)
            ticket.accessed_by = profile
            # ticket.status = 'Accepted'
            ticket.save()
            return redirect('opentickets')

    context = {'form' : form1}
    return render(request, 'greet/ticketupdate.html', context)

