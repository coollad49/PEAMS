from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.
@login_required
def index(request):

    return render(request, 'peams_app/home.html')


def login_view(request):
    if request.method == "POST":
        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "peams_app/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "peams_app/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))

def tracker(request):

    return render(request, 'peams_app/tracker.html')

def notify(request):

    return render(request, 'peams_app/notify.html')