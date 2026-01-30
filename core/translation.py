from modeltranslation.translator import translator, TranslationOptions
from .models import SiteSettings, VisionSection, CoreValue


class SiteSettingsTranslationOptions(TranslationOptions):
    fields = ('site_name', 'address')


class VisionSectionTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

class CoreValueTranslationOptions(TranslationOptions):
     fields = ('title', 'description')


translator.register(SiteSettings, SiteSettingsTranslationOptions)
translator.register(VisionSection, VisionSectionTranslationOptions)
translator.register(CoreValue, CoreValueTranslationOptions)