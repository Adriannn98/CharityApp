from django.shortcuts import render

# Create your views here.
from django.views import View

from charity_app.models import Institution, Donation


class LandingPageView(View):
    def get(self, request):
        donations = Donation.objects.all()
        foundations = Institution.objects.filter(type=1)
        non_gov_orgs = Institution.objects.filter(type=2)
        local_collections = Institution.objects.filter(type=3)
        bags = 0
        organizations_donated = []
        for donation in donations:
            bags += donation.quantity
            if donation.institution not in organizations_donated:
                organizations_donated.append(donation.institution)

        return render(request, 'index.html', { "bags": bags, "organizations_donated_amount": len(organizations_donated),
                                            "foundations": foundations, "non_gov_orgs": non_gov_orgs, "local_collections": local_collections,})

class RegisterView(View):

    def get(self, request):
        return render(request, 'register.html')

class LoginView(View):

    def get(self, request):
        return render(request, 'login.html')

class AddDonationView(View):

    def get(self, request):
        return render(request, 'form.html')