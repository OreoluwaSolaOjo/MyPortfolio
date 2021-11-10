
from django.urls import path, include
from .import views

urlpatterns = [
    path('', views.index),
    path('restaurant/', views.restaurant, name='restaurant'),
    path('fitnessbyore/', views.fitnessbyore, name='fitnessbyore'),
    path('galaxybyosg/', views.galaxybyosg, name='galaxybyosg'),
    path('bmicalculator/', views.bmicalculator, name='bmicalculator'),
    path('thankyoupage/', views.thankyoupage, name='thankyoupage'),
    path('index', views.index, name='index'),

]
