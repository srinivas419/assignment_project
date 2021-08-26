from django.urls import path
from . import views

urlpatterns = [
    path('home_page', views.home),
    path('about_us', views.about),
    path('courses', views.courses),
    path('gallery', views.gallery),
    # path('logpage', views.log_in_page)
]
