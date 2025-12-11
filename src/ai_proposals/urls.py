# ai_proposals/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.app_hub, name="app_hub"),                    # /apps/
    path("proposal/", views.proposal_dashboard, name="proposal_dashboard"),  # /apps/proposal/
]

