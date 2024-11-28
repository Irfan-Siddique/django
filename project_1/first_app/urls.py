from django.urls import path
from . import views
urlpatterns = [
    path("courses/",views.courses),
    path("abouts/", views.abouts),
    path("",views.home),
]