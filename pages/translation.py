from modeltranslation.translator import translator, TranslationOptions
from .models import Page, HeroSection, AboutSection


class PageTranslationOptions(TranslationOptions):
    fields = ('title', 'content')



class HeroSectionTranslationOptions(TranslationOptions):
    fields = ('title', 'subtitle', 'button_text')


class AboutSectionTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

translator.register(Page, PageTranslationOptions)
translator.register(HeroSection, HeroSectionTranslationOptions)
translator.register(AboutSection, AboutSectionTranslationOptions)