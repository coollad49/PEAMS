from django.contrib import admin
from django.urls import path
from peams_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('register/', views.register, name='register'),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path('tracker/', views.tracker, name='tracker'),
    path('notifications/', views.notify, name='notify'),
    path('product/', views.products, name="products"),
    path('product/delete/<str:batch_no>', views.delete_product, name="delete-product"),
]
