from django.contrib import admin
from .models import SiteSettings, VisionSection, CoreValue


# Register your models here.
# ---- Admin للـ SiteSettings ----


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ('site_name', 'email', 'phone', 'default_language')

@admin.register(VisionSection)
class VisionSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')



@admin.register(CoreValue)
class CoreValueAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')