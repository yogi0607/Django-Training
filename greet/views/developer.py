from django import forms
from django import contrib
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from greet.models import DevProfile, Ticket
from greet.forms import DeveloperCreationForm, TicketForm

from django.views.generic import TemplateView, ListView, CreateView, UpdateView


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

class DevDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'greet/developerdashboard.html'


class DevOpenTicketView(LoginRequiredMixin, ListView):
    template_name = 'greet/ticket_list.html'
    model = Ticket
    page = 'dev_opentickets'
    extra_context = {'page' : page}

    def get_queryset(self):
        queryset = Ticket.objects.filter(status = 'Open')
        return queryset


class DevAcceptedTicketView(LoginRequiredMixin, ListView):
    template_name = 'greet/ticket_list.html'
    model = Ticket
    page = 'dev_acceptedtickets'
    extra_context = {'page' : page}

    def get_queryset(self):
        queryset = Ticket.objects.filter(accessed_by=self.request.user.devprofile, status = 'Accepted')
        return queryset


class DevCompletedTicketView(LoginRequiredMixin, ListView):
    template_name = 'greet/ticket_list.html'
    model = Ticket
    page = 'dev_completedtickets'
    extra_context = {'page' : page}

    def get_queryset(self):
        queryset = Ticket.objects.filter(accessed_by=self.request.user.devprofile, status = 'Completed')
        return queryset


class DevClosedTicketView(LoginRequiredMixin, ListView):
    template_name = 'greet/ticket_list.html'
    model = Ticket
    page = 'dev_closedtickets'
    extra_context = {'page' : page}

    def get_queryset(self):
        queryset = Ticket.objects.filter(accessed_by=self.request.user.devprofile, status = 'Closed')
        return queryset


class DevUpdateTicketView(LoginRequiredMixin, UpdateView):
    template_name = 'greet/ticket_create.html'
    form_class = TicketForm
    page = 'updateticket'
    extra_context = {'page': page}
    success_url = reverse_lazy('dev_opentickets')

    def get_object(self):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(Ticket, id=id_)

    def form_valid(self, form):
        form.instance.accessed_by = self.request.user.devprofile
        return super().form_valid(form)

