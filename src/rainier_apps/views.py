# rainier_apps/views.py
from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    """
    Log the user out and redirect them to the login page.
    This view accepts GET so you can use a normal <a href> link.
    """
    logout(request)
    return redirect("login")  # "login" is the name of your LoginView URL
