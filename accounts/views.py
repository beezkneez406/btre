from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User

# Create your views here.
def register(request):
    if request.method == 'POST':
        # Get registration information from register form
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Check that the passwords match
        if password == password2:
            # Check that username is unique
            if User.objects.filter(username=username).exists():
                messages.error(request, 'The username already exists!')
                return redirect('register')
            else:
                # Check that the email is not used
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'That email account is in use!')
                    return redirect('register')
                else:
                    # Everything checks out
                    # now create a user
                    user = User.objects.create_user(first_name=first_name, last_name=last_name,
                                                    username=username, email=email, password=password)
                    user.save()
                    messages.success(request, 'You are now registered and may log in')
                    return redirect('login')
        else:
            # if passwords do not match, throw an error
            # and redirect back to the register page
            messages.error(request, 'Passwords do not match!')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')

def login(request):
    if request.method == 'POST':
        # Get login information from the login form
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            # user exists attempt to login
            auth.login(request, user)
            messages.success(request, 'You are now logged in!')
            return redirect('dashboard')
        else:
            # user was unable to login
            messages.error(request, 'Login unsuccessful, check username/password.')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    return redirect('index')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')