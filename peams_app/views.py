from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.db import IntegrityError
from django.urls import reverse
from django.utils import timezone
from datetime import timedelta
from .models import Product, User
from datetime import datetime
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
            return HttpResponseRedirect(reverse("home"))
        else:
            return render(request, "peams_app/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "peams_app/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "peams_app/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, password)
            user.save()
        except IntegrityError:
            return render(request, "peams_app/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("home"))
    else:
        return render(request, "peams_app/register.html")


def tracker_update():
    today = timezone.now().date()
    one_month_later = today + timedelta(days=30)
    items_to_update = Product.objects.filter(expiry_date__lte=one_month_later, about_to_expire=False)

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

    if request.method == "POST":
        product_name = request.POST["product"]
        expiry = request.POST["expiry"]
        
        try:
            expiry_date = datetime.strptime(expiry, '%Y-%m-%d').date()
        except ValueError:
            # Handle the error if the date format is incorrect
            return render(request, 'your_template.html', {'error': 'Invalid date format. Please use YYYY-MM-DD.'})

        product = Product(name=product_name, expiry_date=expiry_date)

        # Check if the product already exists based on name and expiry_date
        if not products.filter(name=product_name, expiry_date=expiry_date).exists():
            product.save()

    context = {
        'products' : products,
    }
    return render(request, 'peams_app/product.html', context)

def delete_product(request, batch_no):
    product = Product.objects.get(batch_no=batch_no)
    product.delete()
    return HttpResponseRedirect(reverse("products"))