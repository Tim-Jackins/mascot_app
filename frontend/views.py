from django.shortcuts import render
from django.views.generic import TemplateView


def index(request):
  return render(request, 'frontend/index.html')


class AboutPageView(TemplateView):
  template_name = 'pages/about.html'
