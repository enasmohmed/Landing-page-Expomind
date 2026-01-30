from django.views.generic import TemplateView
from pages.models import HeroSection, AboutSection
from core.models import VisionSection, CoreValue, SiteSettings
from services.models import Service
from contact.models import ContactMessage


class HomeView(TemplateView):
    template_name = 'pages/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['hero'] = HeroSection.objects.filter(is_active=True).first()
        context['about'] = AboutSection.objects.filter(is_active=True).first()
        context['vision'] = VisionSection.objects.filter(is_active=True).first()

        context['core_values'] = CoreValue.objects.all()[:4]
        context['services'] = Service.objects.filter(is_active=True).order_by('order')
        context['contact'] = ContactMessage.objects.first()
        # context['site_settings'] = SiteSettings.objects.first()

        return context
