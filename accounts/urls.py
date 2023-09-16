from django.shortcuts import render
from . import views
from django.urls import path, re_path

app_name = "accounts"

urlpatterns = [
    re_path(r"^signup/$", views.signup_view, name="signup"),
]