from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from site_module.models import SiteSettings, FooterLinkBox, Slider


class HomeView(TemplateView):
    template_name = 'home_module/index_page.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sliders'] = Slider.objects.filter(is_active=True)
        return context
def site_header_component(request):
    setting = SiteSettings.objects.filter(is_main_setting=True).first()
    context = {'site_setting': setting}
    return render(request, 'shared/site_header_component.html',context)

def site_footer_component(request):
    setting = SiteSettings.objects.filter(is_main_setting=True).first()
    footer_link_boxes = FooterLinkBox.objects.all()
    for item in footer_link_boxes:
        item.footerlink_set
    context = {'site_setting': setting,'footer_link_boxes':footer_link_boxes}
    return render(request, 'shared/site_footer_component.html',context)

class AboutView(TemplateView):
    template_name = 'home_module/about_page.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        site_setting = SiteSettings.objects.filter(is_main_setting=True).first()
        context['site_setting'] = site_setting
        return context
