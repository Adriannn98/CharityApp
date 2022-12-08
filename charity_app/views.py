from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View

from charity_app.forms import RegisterForm, LoginForm
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
        form = RegisterForm()
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data['password1']
            user.set_password(password)
            user.username = form.cleaned_data['email']
            user.save()
            return redirect('login')
        return render(request, 'register.html', {'form': form})
class LoginView(View):

    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is None:
                return render(request, 'register.html', {'form': form, 'message': "Niepoprawne dane"})
            else:
                login(request, user)
                url = request.GET.get('next', 'landing_page')
                return redirect(url)
        return render(request, 'index.html', {'form': form, 'message': "Zalogowano"})

class LogOutView(View):

    def get(self, request):
        logout(request)
        return redirect('landing_page')

class AddDonationView(View):

    def get(self, request):
        return render(request, 'form.html')