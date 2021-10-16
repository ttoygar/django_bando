from django.shortcuts import render, redirect
from django.http import HttpResponse


def landing_page(request):
    # return HttpResponse("Hey")
    # return render(request, "lp/home.html")
    # permissions = request.user.get_user_permissions()

    # redirects user
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return redirect('/admin/')
        return render(request, "lp/home.html")
    else:
        return redirect('/login/')
