from django import forms
from django import contrib
from django.contrib import auth
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from greet.models import DevProfile, PMProfile, Ticket
# from django.contrib.auth.forms import UserCreationForm
from .forms import ManagerCreationForm, DeveloperCreationForm, TicketForm


# Create your views here.

def home(request):
    return render(request, 'greet/home.html')


def loginmanager(request):
    page = 'pmlogin'

    if request.user.is_authenticated:
        return redirect('pmdashboard')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = PMProfile.objects.get(username=username)
        except:
            messages.error(request, 'Username does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_manager:
            login(request, user)
            return redirect('pmdashboard')
        else:
            messages.error(request, 'Username or password is incorrect')

    return render(request, 'greet/pmlogin.html')


def logoutmanager(request):
    logout(request)
    messages.error(request, 'User was logged out')
    return redirect('pmlogin')


def signupmanager(request):
    page = 'pmsignup'
    form = ManagerCreationForm()

    if request.user.is_authenticated:
        return redirect('pmdashboard')

    if request.method == 'POST':
        form = ManagerCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            user.save()

            messages.success(request, 'User account was created!')

            login(request, user)
            return redirect('pmlogin')

        else:
            messages.success(request, 'An error has occured during registration')

    context = {'page': page, 'form': form}
    return render(request, 'greet/pmlogin.html', context)

@login_required(login_url='pmlogin')
def pmdashboard(request):
    return render(request, 'greet/managerdashboard.html')


@login_required(login_url='pmlogin')
def pm_openTickets(request):
    page = 'pm_open_tickets'
    tickets = Ticket.objects.all()
    open_tickets = tickets.filter(status = 'Open')
    context = {'tickets':tickets, 'open_tickets': open_tickets, 'page':page}
    return render(request, 'greet/alltickets.html', context)

@login_required(login_url='pmlogin')
def pm_acceptedTickets(request):
    page = 'pm_accepted_tickets'
    tickets = Ticket.objects.all()
    profile = request.user.pmprofile
    open_tickets = tickets.filter(status = 'Accepted', user = profile)
    context = {'tickets':tickets, 'open_tickets': open_tickets, 'page':page}
    return render(request, 'greet/alltickets.html', context)

@login_required(login_url='pmlogin')
def pm_completedTickets(request):
    page = 'pm_completed_tickets'
    tickets = Ticket.objects.all()
    profile = request.user.pmprofile
    open_tickets = tickets.filter(status = 'Completed', user = profile)
    context = {'tickets':tickets, 'open_tickets': open_tickets, 'page':page}
    return render(request, 'greet/alltickets.html', context)

@login_required(login_url='pmlogin')
def pm_closedTickets(request):
    page = 'pm_closed_tickets'
    tickets = Ticket.objects.all()
    profile = request.user.pmprofile
    open_tickets = tickets.filter(status = 'Closed', user = profile)
    context = {'tickets':tickets, 'open_tickets': open_tickets, 'page':page}
    return render(request, 'greet/alltickets.html', context)

# @login_required(login_url='pmlogin')
# def pm_getTickets(request):
#     page = 'pm_get_tickets'
#     tickets = Ticket.objects.all()
#     context = {'tickets':tickets, 'page':page}
#     return render(request, 'greet/alltickets.html', context)


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

@login_required(login_url='pmlogin')
def createTicket(request):
    form = TicketForm()
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user.pmprofile
            ticket.save()
            return redirect('pmdashboard')
    context = {'form' : form}
    return render(request, 'greet/ticket_form.html', context)

@login_required(login_url='pmlogin')
def viewTickets(request):
    page = 'viewticket'
    all_tickets = Ticket.objects.all()
    profile = request.user.pmprofile
    tickets = all_tickets.filter(user = profile)
    context = {'all_tickets':all_tickets, 'tickets': tickets, 'page': page}
    return render(request, 'greet/alltickets.html', context)

@login_required(login_url='pmlogin')
def updatepm(request, pk):
    ticket = Ticket.objects.get(id=pk)
    profile = request.user.pmprofile
    form1 = TicketForm(instance=ticket)
    if request.method == 'POST':
        form1 = TicketForm(request.POST, instance=ticket)
        if form1.is_valid():
            ticket = form1.save(commit=False)
            ticket.user = profile
            # ticket.status = 'Accepted'
            ticket.save()
            return redirect('viewticket')

    context = {'form' : form1}
    return render(request, 'greet/ticketupdate.html', context)

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

# @login_required(login_url='devlogin')
# def getTickets(request):
#     tickets = Ticket.objects.all()
#     context = {'tickets':tickets}
#     return render(request, 'greet/ticketList.html', context)
