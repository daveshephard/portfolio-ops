# rainier_apps/urls.py
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path

def home(request):
    return HttpResponse("Rainier Portfolio Ops Demo is running 🚀")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),  # this is your `/`
]