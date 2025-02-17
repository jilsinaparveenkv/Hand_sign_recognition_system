
from django.contrib import admin
from django.urls import path, include

from my_app import views

urlpatterns = [
    path('',views.login),
    path('adminhome',views.adminhome),
    path('experthome',views.experthome),
    path('logincode',views.logincode),
    path('addexpert',views.addexpert),
    path('addsignlanguage',views.addsignlanguage),
    path('blockunblock',views.blockunblock),
    path('complaintReplay',views.complaintReplay),
    path('managexpert',views.managexpert),
    path('managesignlanguage',views.managesignlanguage),
    path('viewcomplaint',views.viewcomplaint),
    path('viewfeedback',views.viewfeedback),



]
