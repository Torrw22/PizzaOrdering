from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns=[
    path("say-hi", views.Greeting),
    path("hello-again", views.otherGreeting),
    path("", views.calculateSelection),
    path("display", views.displaySelection),
    path('admin/', admin.site.urls),
    path('order/', views.order_pizza, name='order_pizza'),
    path('thank_you/', views.thank_you, name='thank_you'),
    ]