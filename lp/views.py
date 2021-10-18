from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib import messages

from lp.forms import SignUpForm, ChangePassForm


def landing_page(request):
    """
    View for landing page. Responsible to redirecting admin to the admin page.
    """
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return redirect('/admin/')
        return render(request, "lp/home.html")
    return redirect('/login/')


def signup(request):
    """View for user self-registration and sending welcome mails."""
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():

            username = form.cleaned_data.get('username')

            if User.objects.filter(username=username).first():
                messages.error(request, "This username is already taken")
                return redirect('/login/')

            raw_password = form.cleaned_data.get('password1')
            email = form.cleaned_data.get('email')
            form.save()

            # Welcome mail
            send_mail(
                'BAŞLIK',
                f'Welcome to the site {username}!',
                'admin@deneme.den',
                [email],
                fail_silently=False,
            )
            user = authenticate(username=username,
                                password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()

    return render(request, 'signup.html', {'form': form})


def change_pass(request):
    """View for user password changing page."""
    if request.user.is_authenticated:
        user_id = request.user.id
        if request.method == 'POST':
            form = ChangePassForm(request.POST)
            if form.is_valid():
                raw_password = form.cleaned_data.get('password1')
                u = User.objects.get(id=user_id)
                u.set_password(raw_password)
                u.save()
                messages.success(request, 'Password successfully changed')
        else:
            form = ChangePassForm()

        return render(request, 'change_pass.html', {'form': form})
    return redirect('/login/')
