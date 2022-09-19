from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.
# Custom Django TemplateView which takes care of rendering the template for home.html
class HomePageView(TemplateView):
  template_name = 'home.html'
  
class AboutPageView(TemplateView):
  template_name = 'about.html'