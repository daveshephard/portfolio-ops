# ai_proposals/views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def app_hub(request):
    """
    App hub showing a grid of available apps.
    For now, only 'Proposal Assistant' is available.
    """
    apps = [
        {
            "name": "Proposal Assistant",
            "slug": "proposal",
            "description": "Use AI to generate and assemble RFP responses from your content library.",
            "status": "Available",
            "url_name": "proposal_dashboard",
        },
        # later you can add more apps here
    ]
    return render(request, "app_hub.html", {"apps": apps})



@login_required
def proposal_dashboard(request):
    """
    Main Proposal Assistant dashboard.
    (You can extend this later to actually call your AI backend.)
    """
    context = {
        "user": request.user,
        "sample_templates": [
            "Generic RFP Response",
            "Healthcare Payer Proposal",
            "Public Sector RFP Template",
        ],
    }
    return render(request, "ai_proposals/proposal_dashboard.html", context)
