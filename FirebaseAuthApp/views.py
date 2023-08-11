from django.shortcuts import render, redirect
import firebase_admin
from firebase_admin import auth
from .forms import *
from firebase_admin.auth import UserNotFoundError
from django.contrib.auth.decorators import login_required
import pyrebase


# Create your views here.

config = {
    "apiKey": "AIzaSyCqiQK6WX9R-RK9gd8LQhNnhg7qkcyBc-8",
    "authDomain": "fir-authproject-15f8f.firebaseapp.com",
    "projectId": "fir-authproject-15f8f",
    "databaseURL": "https://fir-authproject-15f8f-default-rtdb.firebaseio.com",
    "storageBucket": "fir-authproject-15f8f.appspot.com",
    "messagingSenderId": "153096973347",
    "appId": "1:153096973347:web:25003863aca9ee969b9596"
}



def user_register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user_email = form.cleaned_data['user_email']
            user_password = form.cleaned_data['user_password']
            try:
                auth.get_user_by_email(user_email)
                message = "User with this email already exists."
                return render(request, 'registration/user_register.html', {'form': form, 'message': message})
            except UserNotFoundError:
                try:
                    user = auth.create_user(
                        email=user_email,
                        password=user_password,
                    )
                    message = "Registered successfully"
                    return render(request, 'registration/user_register.html', {"form": form, "message": message})
                except auth.AuthError as e:
                    return render(request, "registration/user_register.html", {"form": form, "message": e})
    else:
        form = UserForm()
    return render(request, 'registration/user_register.html', {'form': form})


@login_required
def home_page(request):
    user = auth.get_account_info(request.session['uid'])
    user_data = user['users'][0]['providerUserInfo'][0]
    context = {
        'user_data': user_data,
    }
    return render(request, 'registration/home_page.html', context)



def user_login(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user_email = form.cleaned_data['user_email']
            user_password = form.cleaned_data['user_password']
            try:
                # Sign in the user with email and password
                user = auth.sign_in_with_email_and_password(user_email, user_password)
                message = "Login successful"
                
                return render(request, "registration/user_login.html", {"form": form, "message": message})
            except auth.AuthError as e:
                message = "Login failed: " + str(e)
                return render(request, "registration/user_login.html", {"form": form, "message": message})
    else:
        form = UserForm()
    return render(request, 'registration/user_login.html', {'form': form})



def password_reset(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            auth.send_password_reset_email(email)
            message = 'Password reset email sent. Please check your inbox.'
            return render(request, 'registration/password_reset.html', {"message":message})
        except:
            message = 'Password reset failed. Please try again.'
    return render(request, 'registration/password_reset.html', {'message': message})

def user_profile(request):
    user = auth.get_account_info(request.session['uid'])  # Fetch user information from Firebase
    user_data = user['users'][0]['providerUserInfo'][0]
    return render(request, 'registration/user_profile.html', {'user_data': user_data})

def user_logout(request):
    auth.logout(request)
    request.session.pop('uid', None)  # Remove Firebase UID from session
    return redirect('registration/login')