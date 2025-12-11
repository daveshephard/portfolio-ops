# rainier_apps/urls.py
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from .views import logout_view  # <-- import the custom logout

urlpatterns = [
    # Landing page = login
    path(
        "",
        auth_views.LoginView.as_view(template_name="registration/login.html"),
        name="login",
    ),

    # Use custom logout view instead of LogoutView
    path("logout/", logout_view, name="logout"),

    # App hub + proposal assistant
    path("apps/", include("ai_proposals.urls")),

    path("admin/", admin.site.urls),
]
