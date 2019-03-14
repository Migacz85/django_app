from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from Home.forms import UserLoginForm


def home(request):

    # messages.success(request, 'Welcome in Unicorn attractor')
    return render(request, 'home.html')


def logout(request):
    """Log the user out"""
    auth.logout(request)
    messages.success(request, ' You have successfully been logout')

    # How to access 2 messages from django templates ?
    # messages.info(request, 'We will wait for you till next time')
    return redirect(reverse('home'))


def login(request):
    """Return a login page"""
    if request.user.is_authenticated:
        messages.info(request, 'You are already loged in')
        return redirect(reverse('home'))

    if request.method == "POST":
        login_form = UserLoginForm(request.POST)
        if login_form.is_valid():
            user = auth.authenticate(
                username=request.POST['username'],
                password=request.POST['password'])

            if user:
                messages.success(
                    request,
                    "You have successfully logged in!"
                                 )
                auth.login(user=user, request=request)
                return redirect(reverse('home'))
            else:
                login_form.add_error(
                    None,
                    "Your username or password is not valid"
                                     )
    else:
        login_form = UserLoginForm()
    return render(request, 'login.html', {"login_form": login_form})


def register(request):
    """Let user to register"""
    return render(request, 'registration.html')
