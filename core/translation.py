from modeltranslation.translator import translator, TranslationOptions
from .models import SiteSettings, VisionSection, CoreValue, CTASection, FooterSection, Sections


class SiteSettingsTranslationOptions(TranslationOptions):
    fields = ('site_name', 'address')


class FooterSectionTranslationOptions(TranslationOptions):
    fields = ('site_name', 'description' ,'address', 'copyright_text', 'working_days', 'working_hours', 'sunday_hours')

class VisionSectionTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

class CoreValueTranslationOptions(TranslationOptions):
     fields = ('title', 'description')

class SectionsTranslationOptions(TranslationOptions):
     fields = ('title', 'slug')


class CTASectionTranslationOptions(TranslationOptions):
    fields = ('title', 'button_text')


translator.register(SiteSettings, SiteSettingsTranslationOptions)
translator.register(FooterSection, FooterSectionTranslationOptions)
translator.register(VisionSection, VisionSectionTranslationOptions)
translator.register(CoreValue, CoreValueTranslationOptions)
translator.register(CTASection, CTASectionTranslationOptions)
translator.register(Sections, SectionsTranslationOptions)