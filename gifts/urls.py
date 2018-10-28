"""
defines URL patterns for gifts

"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('gifts/current', views.gifts_for_current_year, name='gifts_current'),
    path('gifts/all', views.all_gifts, name='gifts_all'),
    path('gifts/<str:name>/', views.gifts_by_person, name='gifts_by_person'),
    path('gifts/from/<str:name_from>/', views.gifts_by_giver, name='gifts_by_from'),
    path('gifts/to/<str:name_to>/', views.gifts_by_recipent, name='gifts_by_recipient'),
]
