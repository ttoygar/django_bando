from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

from lp.forms import SignUpForm


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
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            # email = form.cleaned_data.get('email')
            user = authenticate(username=username, password=raw_password) #, email=email)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
        # print([field.name for field in form])

    return render(request, 'signup.html', {'form': form})
