from django.shortcuts import render
from django.http import HttpResponse


def landing_page(request):
    # return HttpResponse("Hey")
    return render(request, "lp/home.html")
