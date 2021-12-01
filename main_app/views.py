from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Models
from main_app.models import User, Portfolio, Stock

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

### PROFILE VIEWS ###
class ProfileDetail(DetailView):
    # Adds context["user"]
    model = User
    template_name = "profile_detail.html"

# Too hard: Change to add & delete buttons
# class ProfileUpdate(View):
#     template_name = "profile_update.html"

### PORTFOLIO VIEWS ###
class PortfolioList(TemplateView):
    template_name = "portfolio_list.html"
    
    # Adds portfolios to context
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["portfolios"] = Portfolio.objects.all()
        return context

class PortfolioDetail(DetailView):
    # Adds context["portfolio"] = Portfolio.objects.get(pk=pk)
    # pk comes from url
    model = Portfolio
    template_name = "portfolio_detail.html"

class PortfolioCreate(CreateView):
    model = Portfolio
    fields = "__all__"
    template_name = "portfolio_create.html"
    def get_success_url(self): 
      return reverse("portfolio_detail", kwargs={"pk": self.object.pk})

class PortfolioUpdate(UpdateView):
    model = Portfolio
    fields = "__all__"
    template_name = "portfolio_update.html"

    # FIXME: Fails to redirect
    def get_success_url(self): 
      return reverse("portfolio_detail", kwargs={"pk": self.object.pk})

### STOCK Views
class StockCreate(CreateView):
    model = Stock
    fields = '__all__'
    template_name = "stock_create.html"
    
    def get_success_url(self):
        return reverse("portfolio_detail", kwargs={"pk": self.object.portfolio.id})


# NOTE
### CreateView: needs to define fields
### https://stackoverflow.com/questions/46701426/using-modelformmixin-without-the-fields-attribute-is-prohibited