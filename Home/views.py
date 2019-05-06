from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from Home.forms import UserLoginForm, UserRegistrationForm
from bugs.models import Issues

def home(request):
    """Home page"""

    issue = Issues.objects.filter(
        issue_type='Feature'
    ).order_by('-published_date')

    return render(request, 'home.html')


@login_required
def logout(request):
    """Log the user out"""
    auth.logout(request)
    messages.success(request, ' You have successfully been logout')

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
    return render(request, 'login.html',
                  {"login_form": login_form,
                   }
                  )


def register(request):
    """Let user to register"""

    if request.user.is_authenticated:
        return redirect(reverse('home'))

    if request.method == "POST":

        registration_form = UserRegistrationForm(request.POST)

        if registration_form.is_valid():
            registration_form.save()

        user = auth.authenticate(
            username=request.POST['username'],
            password=request.POST['password1']
        )

        if user:
            auth.login(user=user, request=request)
            messages.success(request, "You have successfully registered")
            return redirect(reverse('home'))
        else:
            messages.error(
                request,
                "There were errors registering your account. Try again."
            )
    else:
        registration_form = UserRegistrationForm()

    return render(
        request,
        'registration.html',
        {"registration_form": registration_form}
    )


@login_required
def user_profile(request):
    """The user's profile page"""
    user = User.objects.get(email=request.user.email)

    return render(
        request,
        'user_profile.html',
        {"profile": user}
    )
