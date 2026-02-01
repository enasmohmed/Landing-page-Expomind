from django.core.cache import cache
from .models import SiteSettings, FooterSection, SocialMedia


def site_settings_context(request):
    site = SiteSettings.objects.first()

    data = {
        'site_name': site.site_name if site else '',
        'primary_color': site.primary_color if site else '#000000',
        'secondary_color': site.secondary_color if site else '#ffffff',
        'website': site.website if site else '',
        'phone': site.phone if site else '',
        'email': site.email if site else '',
        'facebook': site.facebook if site else '',
        'linkedin': site.linkedin if site else '',
        'instagram': site.instagram if site else '',

        'logo_url': (
            site.logo.url
            if site and site.logo
            else '/static/images/default-logo.png'
        ),

        'favicon_url': (
            site.favicon.url
            if site and site.favicon
            else '/static/images/favicon.ico'
        ),
    }

    footer = FooterSection.objects.filter(is_active=True).first()
    social_links = SocialMedia.objects.filter(is_active=True)

    return {
        'site_settings': data,
        'footer': footer,
        'logo_url': data['logo_url'],
        'favicon_url': data['favicon_url'],
        'social_links': social_links,
    }
