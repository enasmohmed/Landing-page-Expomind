
from django.views.generic import TemplateView
from pages.models import HeroSection, AboutSection, WhoWeAreSection
from core.models import VisionSection, CoreValue, SiteSettings, CTASection, Sections
from services.models import Service
from contact.models import ContactMessage


class HomeView(TemplateView):
    template_name = 'pages/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['hero'] = HeroSection.objects.filter(is_active=True).first()
        context['about'] = AboutSection.objects.filter(is_active=True).first()
        context['who_we_are'] = WhoWeAreSection.objects.filter(is_active=True).first()
        context['sections'] = Sections.objects.filter(show_in_nav=True).order_by('order')

        context['mission'] = VisionSection.objects.filter(
            is_active=True,
            section_type='mission'
        ).first()

        context['vision'] = VisionSection.objects.filter(
            is_active=True,
            section_type='vision'
        ).first()

        context['core_values'] = CoreValue.objects.all()

        context['services'] = Service.objects.filter(is_active=True).order_by('order')
        context['contact'] = ContactMessage.objects.first()
        context['cta'] = CTASection.objects.filter(is_active=True).first()
        return context
