from django.http import HttpResponse
from django.urls import path

from djangoUrlsAndViews.departments import views

urlpatterns = [
    path('', views.index),
    path('<int:pk>/', views.view_with_int_pk),
    path('<variable>/', views.view_with_name),
]









