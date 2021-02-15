from django.contrib.auth import login, authenticate,logout
from django.shortcuts import render, redirect
from accounts.forms import SignUpForm,TherapistSignupForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.db import transaction
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from therapist_dashboard.views import ProfileView
from .models import Therapist

#from .decorators import allowed_users,unauthenticated_users


#@allowed_users(allowed_roles=['forum_users','Admin users'])
def home(request):
    return render(request, 'accounts/home.html')

#@unauthenticated_users
def signup(request):
    form=SignUpForm
    
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():

            user = form.save()

            user.refresh_from_db()  # load the profile instance created by the signal
            user.is_normal_user=True
            user.profile.user_name=form.cleaned_data.get('username')
            user.profile.email_id=form.cleaned_data.get('email')
            user.profile.first_name=form.cleaned_data.get('first_name')
            user.profile.last_name=form.cleaned_data.get('last_name')
            user.profile.date_of_birth = form.cleaned_data.get('date_of_birth')
            user.profile.location = form.cleaned_data.get('location')
            user.profile.reason = form.cleaned_data.get('reason')
            user.profile.superuser=False
            user.profile.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})


def therapist_signup(request):
    form=TherapistSignupForm
    if request.method == 'POST':
        form = TherapistSignupForm(request.POST)
        if form.is_valid():
            
            user = form.save(commit=False)
            user.is_normal_user=False
            user.save()

            user.refresh_from_db()  # load the profile instance created by the signal
            user.username=form.cleaned_data.get('username')
            user.therapist.therapist_name=form.cleaned_data.get('name')
            user.therapist.therapist_email=form.cleaned_data.get('email')
            user.therapist.office_address=form.cleaned_data.get('office_address')
            user.therapist.qualification=form.cleaned_data.get('qualification')
            user.therapist.specialization_area = form.cleaned_data.get('specialization_area')
            user.therapist.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('therapist_dashboard:home')
    else:
        form = TherapistSignupForm()
    return render(request, 'accounts/therapist_signup.html', {'form': form})



def login_request(request):
    
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:

                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                if user.is_normal_user==True:
                    return redirect('home')
                else:
                    return redirect('therapist_dashboard:home')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request = request,
                    template_name = "accounts/login.html",
                    context={"form":form})


def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect('login')

