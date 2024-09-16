from django.urls import path, re_path, include
from djangoUrlsAndViews.departments import views

urlpatterns = [
    path('', views.index, name='home'),
    path('redirect/', views.redirect_to_view, name='redirect-view'),
    path('numbers/', include([
        path('<int:pk>/', views.view_with_int_pk),
        path('<int:pk>/<slug:slug>/', views.view_with_slug),
    ])),
    path('<variable>/', views.view_with_name),  # Matches till /
    re_path(r'^archive/(?P<archive_year>202[0-3])/$', views.show_archive),
    # path('<path:variable>/', views.view_with_name), # Matches after the / as well
    # path('<uuid:id>/', some_view),
]










