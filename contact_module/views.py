from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.edit import FormView

from .forms import ContactForm
# Create your views here.

class ContactUsView(FormView):
    form_class = ContactForm
    template_name = 'contact_module/contact_us_page.html'
    success_url = reverse_lazy('contact_us')
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
# class ContactUsView(View):
#     def get(self, request):
#         contact_form = ContactUsForm()
#         return render(request,'contact_module/contact_us_page.html',context={'contact_form':contact_form})
#
#     def post(self, request):
#         contact_form = ContactUsForm(request.POST)
#         if contact_form.is_valid():
#             contact_form.save()
#             return redirect('home_page')
#         return render(request, 'contact_module/contact_us_page.html', context={'contact_form': contact_form})