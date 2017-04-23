from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.


class HomePageView(TemplateView):
    template_name = "home_app/home/index.html"

    def get_context_data(self, **kwargs):
        pass
