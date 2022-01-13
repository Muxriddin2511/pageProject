from django.shortcuts import render
from django.views.generic import TemplateView

class SahifaPageView(TemplateView):
    template_name = "sahifa.html"
class HomePageView(TemplateView):
    template_name = "home.html"
class AboutpageView(TemplateView):
    template_name = "about.html"
