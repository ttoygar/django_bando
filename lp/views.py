from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib import messages

from lp.forms import SignUpForm, ChangePassForm


def landing_page(request):
    # redirects user
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return redirect('/admin/')
        return render(request, "lp/home.html")
    else:
        return redirect('/login/')


def signup(request):
    # if request.method == 'POST':
    #     form = UserCreationForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         username = form.cleaned_data.get('username')
    #         raw_password = form.cleaned_data.get('password1')
    #         user = authenticate(username=username, password=raw_password)
    #         login(request, user)
    #         return redirect('home')
    # else:
    #     form = UserCreationForm()
    # return render(request, 'signup.html', {'form': form})

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
            send_mail(
                'BAŞLIK',
                f'Hoşgeldin {username}!',
                'admin@deneme.den',
                [email],
                fail_silently=False,
            )
            user = authenticate(username=username,
                                password=raw_password)  # , email=email)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
        # print([field.name for field in form])

    return render(request, 'signup.html', {'form': form})


def change_pass(request):
    if request.user.is_authenticated:
        username = request.user.username
        id = request.user.id
        if request.method == 'POST':
            form = ChangePassForm(request.POST)
            if form.is_valid():
                raw_password = form.cleaned_data.get('password1')
                # u = User.objects.get(username=username)
                u = User.objects.get(id=id)
                u.set_password(raw_password)
                u.save()
                messages.success(request, 'Şifre başarıyla değiştirildi')
        else:
            form = ChangePassForm()

        return render(request, 'change_pass.html', {'form': form})
    # else:
    return redirect('/login/')
