from sys import path_hooks

from django.urls import path, include
from petstagram.accounts import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.login, name='register'),
    path('profile/<int:pk>/', include([
        path('', views.profile_details_page, name='profile-details'),
        path('edit', views.profile_edit_page, name='profile-edit'),
        path('delete', views.profile_delete_page, name='profile-delete'),
    ])),
]