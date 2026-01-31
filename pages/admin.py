from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Page, HeroSection, AboutSection, WhoWeAreSection, WhoWeAreFeature


# ---- Admin للـ Page ----
@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'is_active', 'language')
    search_fields = ('title', 'content')
    list_filter = ('is_active', 'language')

@admin.register(HeroSection)
class HeroSectionAdmin(admin.ModelAdmin):
    list_display = ('title',  'is_active', 'language')
    search_fields = ('title', 'subtitle')
    list_filter = ('is_active', 'language')



@admin.register(AboutSection)
class AboutSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'language')
    search_fields = ('title', 'description')
    list_filter = ('is_active', 'language')


@admin.register(WhoWeAreSection)
class WhoWeAreSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'language')
    search_fields = ('title', 'description')
    list_filter = ('is_active', 'language')




@admin.register(WhoWeAreFeature)
class WhoWeAreFeatureAdmin(admin.ModelAdmin):
    list_display = ('name', 'section', )
