from django.db import models

# Create your models here.


from ckeditor.fields import RichTextField



class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    content = RichTextField(blank=True, null=True)
    cover_image = models.ImageField(upload_to='blog/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True)
    language = models.CharField(max_length=5, choices=[('en','English'), ('ar','Arabic')], default='en')

    def __str__(self):
        return f"{self.title} ({self.language})"
