from django.db import models

# Create your models here.


from ckeditor.fields import RichTextField

class Project(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = RichTextField(blank=True, null=True)
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    language = models.CharField(max_length=5, choices=[('en','English'), ('ar','Arabic')], default='en')

    def __str__(self):
        return f"{self.title} ({self.language})"
