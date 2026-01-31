from django.db import models
from django.utils.text import slugify
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



class FooterSection(models.Model):
    # شعار الموقع واسم الموقع
    logo = models.ImageField(upload_to='footer/', blank=True, null=True)
    site_name = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    # ساعات العمل
    working_days = models.CharField(max_length=200, blank=True, null=True)
    working_hours = models.CharField(max_length=100, blank=True, null=True)
    sunday_hours = models.CharField(max_length=100, blank=True, null=True)

    # روابط سريعة
    quick_links = models.JSONField(blank=True, null=True)

    # حلول أو خدمات
    solutions = models.JSONField(blank=True, null=True)

    # Recent Posts
    recent_posts = models.JSONField(blank=True, null=True)

    # بيانات التواصل
    address = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    # حقوق الملكية
    copyright_text = models.TextField(blank=True, null=True)

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Footer - {self.site_name}"



SECTION_TYPE_CHOICES = (
    ('mission', 'Mission'),
    ('vision', 'Vision'),
)

class VisionSection(models.Model):
    section_type = models.CharField(
        max_length=20,
        choices=SECTION_TYPE_CHOICES,
        default='vision'
    )
    title = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    background_image = models.ImageField(upload_to='vision/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    default_language = models.CharField(
        max_length=5,
        choices=[('en', 'English'), ('ar', 'Arabic')],
        default='en'
    )

    def __str__(self):
        return f"{self.section_type} - {self.title}"


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




class CTASection(models.Model):
    title = models.CharField(
        max_length=255,
        help_text="Main CTA heading", blank=True, null=True
    )
    button_text = models.CharField(
        max_length=50,
        help_text="Button label", blank=True, null=True
    )
    button_link = models.CharField(
        max_length=255,
        help_text="URL or anchor (e.g. #contact)", blank=True, null=True
    )

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title



class Sections(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    is_visible = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)
    show_in_nav = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            # نعتمد على العنوان الإنجليزي في الـ slug (أفضل تقنيًا)
            self.slug = slugify(self.title_en)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
