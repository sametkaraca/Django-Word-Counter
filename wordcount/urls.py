from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.main, name='home'),
    path('about/', views.about, name='about'),
    path('count/', views.count, name='count')
]

urlpatterns += staticfiles_urlpatterns()
