from django.db import models
from django.utils.text import slugify
from base.models import BaseModel




class Status(BaseModel):
     icon = models.ImageField(upload_to='status_icon/' ,blank=True, null=True)
     name = models.CharField(max_length=100, unique=True)


     def __str__(self):
          return f'{self.icon} - {self.name}'

class Blog(BaseModel):
     title = models.CharField(max_length=200)
     slug = models.SlugField(unique=True, blank=True)
     subtitle = models.CharField(max_length=200, blank=True, null=True)
     content = models.TextField()
     image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
     author = models.CharField(max_length=100, blank=True, null=True)
     status = models.ForeignKey(Status, on_delete=models.CASCADE, related_name='blog_status', blank=True, null=True)
     views = models.PositiveIntegerField(default=0)
     likes = models.PositiveIntegerField(default=0)
     

     def save(self, *args, **kwargs):
          if not self.slug:
               self.slug = slugify(self.title,  allow_unicode=True)
          return super().save(*args, **kwargs)


     def __str__(self):
          return f'{self.title} - {self.author if self.author else "Unknown Author"}'