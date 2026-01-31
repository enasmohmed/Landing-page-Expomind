from modeltranslation.translator import translator, TranslationOptions
from .models import Page, HeroSection, AboutSection, WhoWeAreSection, WhoWeAreFeature


class PageTranslationOptions(TranslationOptions):
    fields = ('title', 'content')



class HeroSectionTranslationOptions(TranslationOptions):
    fields = ('title', 'subtitle', 'button_text')


class AboutSectionTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


class WhoWeAreSectionTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


class WhoWeAreFeatureTranslationOptions(TranslationOptions):
    fields = ('name',)


translator.register(Page, PageTranslationOptions)
translator.register(HeroSection, HeroSectionTranslationOptions)
translator.register(AboutSection, AboutSectionTranslationOptions)
translator.register(WhoWeAreSection, WhoWeAreSectionTranslationOptions)
translator.register(WhoWeAreFeature, WhoWeAreFeatureTranslationOptions)