from django.urls import path
from django.views.generic import TemplateView

app_name = 'tools'


urlpatterns = [
    path('about/',
         TemplateView.as_view(template_name='tools/about.html'),
         name='about'),
    path('rules/',
         TemplateView.as_view(template_name='tools/rules.html'),
         name='rules'),
]
