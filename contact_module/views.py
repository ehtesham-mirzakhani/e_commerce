from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.edit import  CreateView

from site_module.models import SiteSettings
from .forms import ContactForm
# Create your views here.

class ContactUsView(CreateView):
    form_class = ContactForm
    template_name = 'contact_module/contact_us_page.html'
    success_url = reverse_lazy('contact_us')
    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        site_settings = SiteSettings.objects.filter(is_main_setting=True).first()
        context['site_settings'] = site_settings
        return context

