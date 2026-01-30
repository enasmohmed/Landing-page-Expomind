from django.db import models
from django.utils.translation import gettext_lazy as _

class SiteSettings(models.Model):
    site_name = models.CharField(max_length=255, blank=True, null=True)
    logo = models.ImageField(upload_to='settings/', blank=True, null=True)
    favicon = models.ImageField(upload_to='settings/', blank=True, null=True)
    primary_color = models.CharField(max_length=7, blank=True, null=True)  # HEX
    secondary_color = models.CharField(max_length=7, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    default_language = models.CharField(max_length=5, choices=[('en','English'), ('ar','Arabic')], default='en')

    class Meta:
        verbose_name = _("Site Setting")
        verbose_name_plural = _("Site Settings")

    def __str__(self):
        return self.site_name or "Site Settings"





class VisionSection(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    background_image = models.ImageField(upload_to='vision/', blank=True, null=True)
    is_active = models.BooleanField(default=True, blank=True, null=True)
    default_language = models.CharField(max_length=5, choices=[('en', 'English'), ('ar', 'Arabic')], default='en')

    class Meta:
        verbose_name = _("Vision Section")

    def __str__(self):
        return self.title


class CoreValue(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField()
    icon = models.ImageField(upload_to='icons/', blank=True, null=True)
    order = models.PositiveIntegerField(default=0, blank=True, null=True)

    class Meta:
        ordering = ['order']
        verbose_name = _("Core Value")

    def __str__(self):
        return self.title
