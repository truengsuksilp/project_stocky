from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Models
from main_app.models import Portfolio, Stock

# Auth
from django.contrib.auth import login, authenticate
from .forms import SignUpForm, LoginForm

# Create your views here.
class Home(TemplateView):
    template_name = 'home.html'

    # TODO: Add conditionals - not logged in and valuation not added
    def post(self, request, pk):

        user_id = request.user.id
        stocks = request.POST.get("tickers")
        valuation = request.POST.get("valuation")

        # Split comma separated input
        stock_array = stocks.replace(" ","").split(",")

        # Update DB
        Portfolio.object.create(user_id=user_id, valuation=valuation)

        for i in stock_array:
            Stock.object.create(stock_array[i])

        

class SignUp(View):
    def get(self, request):
        form = SignUpForm()
        context = {'form': form}
        return render(request, 'registration/signup.html', context)

    def post(self, request):
        form = SignUpForm(request.POST)

        if form.is_valid():
            user=form.save()
            login(request, user)
            return redirect('home')
        else: 
            context = {'form': form}
            return render(request,'registration/signup.html', context)