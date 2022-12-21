from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def myHomeView(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    return render(request, "index.html", {})

def aboutUs(request, *args, **kwargs):
    return render(request, "about-us.html", {})

def contacts(request, *args, **kwargs):
    return render(request, "contacts.html", {})

def typography(request, *args, **kwargs):
    return render(request, "typography.html", {})
