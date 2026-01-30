from django.core.cache import cache
from .models import SiteSettings




def site_settings_context(request):
    data = cache.get('site_settings_data')

    if data is None:
        site = SiteSettings.objects.first()

        data = {
            'site_name': site.site_name if site else '',
            'primary_color': site.primary_color if site else '#000000',
            'secondary_color': site.secondary_color if site else '#ffffff',

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

        cache.set('site_settings_data', data, 3600)

    return {
        'site_settings': data,
        'logo_url': data['logo_url'],
        'favicon_url': data['favicon_url'],
    }
