from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home),
    path("display/", views.display_values, name="display_values"),
    # path("rephrase/", views.rephrase, name="rephrase"),
    path("display_data/", views.display_data, name="display_data"),
    # path("search/", views.display_api, name="rephrase"),
]
