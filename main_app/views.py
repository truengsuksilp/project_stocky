from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.
class Home(TemplateView):
    template_name = 'home.html'