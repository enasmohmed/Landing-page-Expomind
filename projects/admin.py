from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Project



@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'category', 'is_active', 'language')
    search_fields = ('title', 'description', 'category')
    list_filter = ('category', 'is_active', 'language')
