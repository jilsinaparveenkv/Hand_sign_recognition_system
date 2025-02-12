
from django.contrib import admin
from django.urls import path, include

from my_app import views

urlpatterns = [
    path('',views.login),
    path('adminhome',views.adminhome),
    path('experthome',views.experthome),
    path('logincode',views.logincode),


]
