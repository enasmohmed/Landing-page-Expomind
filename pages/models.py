from django.db import models
from ckeditor.fields import RichTextField
from django.utils.translation import gettext_lazy as _

# Create your models here.






class Page(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    content = RichTextField(blank=True, null=True)
    template_name = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    language = models.CharField(max_length=5, choices=[('en','English'), ('ar','Arabic')], default='en')

    def __str__(self):
        return f"{self.title} ({self.language})"




class HeroSection(models.Model):
    title = RichTextField(max_length=200, blank=True, null=True)
    subtitle = RichTextField(blank=True, null=True)
    background_image = models.ImageField(upload_to='hero/', blank=True, null=True)
    button_text = models.CharField(max_length=50, blank=True, null=True)
    button_link = models.URLField(blank=True, null=True)

    is_active = models.BooleanField(default=True)
    language = models.CharField(max_length=5, choices=[('en', 'English'), ('ar', 'Arabic')], default='en')

    def __str__(self):
        return f"{self.title} ({self.language})"



class AboutSection(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    description = RichTextField(blank=True, null=True)
    image = models.ImageField(upload_to='about/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    language = models.CharField(max_length=5, choices=[('en', 'English'), ('ar', 'Arabic')], default='en')

    def __str__(self):
        return f"{self.title} ({self.language})"



