from django.shortcuts import render, redirect, get_object_or_404
from .models import User, ServiceRequest
from .forms import UserRegisterForm, ServiceRequestForm,UserServiceRequestForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import login, authenticate,logout
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.sessions.models import Session
from django.contrib.auth.decorators import user_passes_test

def is_agent(user):
    return user.is_admin

def logout_view(request):
    logout(request)
    form = UserRegisterForm()
    return redirect('/')

def login_view(request):
    print("login called")
    next_url = request.GET.get('next', '/')
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password'),
            )
            if user is not None:
                login(request, user)
                if user.is_admin:   
                    service_requests = ServiceRequest.objects.all().order_by('-created_at')
                    return render(request, 'agent_dashboard.html', {'service_requests': service_requests})
                else:
                    print("in service2")
                    return redirect('service_request_list')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})


@login_required
@user_passes_test(is_agent, login_url='login')
def agent_dashboard(request):
    service_requests = ServiceRequest.objects.all().order_by('-created_at')
    total_requests = service_requests.count()
    pending_requests = service_requests.filter(status='Pending').count()
    resolved_requests = service_requests.filter(status='Resolved').count()

    # Pass the data to the template
    context = {
        'service_requests': service_requests,
        'total_requests': total_requests,
        'pending_requests': pending_requests,
        'resolved_requests': resolved_requests,
    }
    return render(request, 'agent_dashboard.html', context)

@login_required
@user_passes_test(is_agent, login_url='login')
def agent_request_detail(request, request_id):
    service_request = get_object_or_404(ServiceRequest, pk=request_id)
    
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, instance=service_request)
        if form.is_valid():
            form.save()
            return redirect('agent_dashboard')
    else:
        form = ServiceRequestForm(instance=service_request)
    return render(request, 'agent_request_detail.html', {'form': form, 'service_request': service_request})
 
@login_required
def service_request_list(request):
    # Filter the service requests by the logged-in user
    service_requests = ServiceRequest.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'service_request_list.html', {'service_requests': service_requests})

@login_required
def service_request_create(request):
    if request.method == 'POST':
        form = UserServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.user = request.user
            service_request.save()
            return redirect('service_request_list')
    else:
        form = UserServiceRequestForm()
    return render(request, 'service_request_form.html', {'form': form})

@login_required
def service_request_edit(request, request_id):
    service_request = get_object_or_404(ServiceRequest, pk=request_id, user=request.user)
    if request.method == "POST":
        form = UserServiceRequestForm(request.POST, request.FILES, instance=service_request)
        if form.is_valid():
            service_request.save()
            return redirect('service_request_list')
    else:
        form = UserServiceRequestForm(instance=service_request)
    return render(request, 'service_request_form.html', {'form': form})

@login_required
def service_request_delete(request, request_id):
    service_request = get_object_or_404(ServiceRequest, pk=request_id, user=request.user)
    if request.method == 'POST':
        service_request.delete()
        return redirect('service_request_list')
    return render(request, 'service_request_confirm_delete.html', {'service_request': service_request})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('service_request_list')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {'form': form})

    