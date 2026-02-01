from django.contrib import admin
from .models import SiteSettings, VisionSection, CoreValue, CTASection, FooterSection, Sections, SocialMedia


# Register your models here.
# ---- Admin للـ SiteSettings ----


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ('site_name', 'email', 'phone', 'default_language')


@admin.register(FooterSection)
class FooterSectionAdmin(admin.ModelAdmin):
    list_display = ('site_name', 'email', 'phone', 'site_name')


@admin.register(VisionSection)
class VisionSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')



@admin.register(CoreValue)
class CoreValueAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')


@admin.register(CTASection)
class CTASectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'button_text', 'is_active')



@admin.register(Sections)
class SectionsAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'is_visible')


@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ('name',  )