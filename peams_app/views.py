from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from datetime import timedelta
from .models import Product
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

def tracker_update():
    today = timezone.now().date()
    one_month_later = today + timedelta(days=30)
    items_to_update = Product.objects.filter(expiry_date=one_month_later, about_to_expire=False)

    for product in items_to_update:
        product.about_to_expire = True
        product.alert_status = "warning"
        product.save()

    items_expired = Product.objects.filter(expiry_date__lt=today, expired=False)
    for product in items_expired:
        product.expired = True
        product.alert_status = "expired"
        product.save()


def tracker(request):
    tracker_update()
    products = Product.objects.all()
    about_to_expire_count = Product.objects.filter(about_to_expire=True).count()
    expired_count = Product.objects.filter(expired=True).count()
    products_notify = Product.objects.exclude(alert_status="okay").count()
    context = {
        'products' : products,
        'about_to_expire': about_to_expire_count,
        'expired': expired_count,
        'notification_count': products_notify,
    }

    return render(request, 'peams_app/tracker.html', context)

def notify(request):
    products = Product.objects.exclude(alert_status="okay")

    context = {
        'products' : products,
    }

    return render(request, 'peams_app/notify.html', context)

def products(request):
    products = Product.objects.all()

    context = {
        'products' : products,
    }
    return render(request, 'peams_app/product.html', context)