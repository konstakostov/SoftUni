from django.urls import path, include
from petstagram.pets import views

urlpatterns = [
    path('add/', views.pet_add_page, name='pet-add'),
    path('<str:username>/pet/<slug:pet_slug>/', include([
        path('', views.pet_details_page, name='pet-details'),
        path('', views.pet_edit_page, name='pet-edit'),
        path('', views.pet_delete_page, name='pet-delete'),
    ]))
]