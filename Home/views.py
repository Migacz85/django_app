from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from Home.forms import UserLoginForm, UserRegistrationForm
from bugs.models import Issues
from django.shortcuts import render_to_response


def home(request):
    """Home page"""

    features = Issues.objects.filter(
        issue_type='Feature', status='Waiting'
    ).order_by('-upvotes')

    bugs = Issues.objects.filter(
        issue_type='Bug', status='Waiting'
    ).order_by('-upvotes')

    return render(request, 'home.html',
                  {'features': features,
                   'bugs': bugs,
                   })


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


def handler404(request, exception, template_name="404.html", ):
    response = render_to_response("404.html")
    response.status_code = 404
    return response


def handler500(request, exception, template_name="500.html"):
    response = render_to_response("500.html")
    response.status_code = 500
    return response
