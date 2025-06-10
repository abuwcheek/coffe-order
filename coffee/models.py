from django.db import models
from django.utils.text import slugify
# from djrichtextfield.models import RichTextField
from ckeditor.fields import RichTextField # Agar rasm yuklash kerak bo'lmasa
from ckeditor_uploader.fields import RichTextUploadingField # <--- Rasm yuklash funksiyasi uchun buni ishlatamiz
from base.models import BaseModel
from blog.models import Status



class CoffeeModel(BaseModel):
     title = models.CharField(max_length=200)
     slug  = models.SlugField(unique=True, blank=True)
     mini_desc = models.CharField(max_length=200)
     description =  RichTextUploadingField()
     image = models.ImageField(upload_to='coffee_images/', null=True, blank=True)
     status = models.ForeignKey(Status, on_delete=models.SET_NULL, related_name='coffee_status', null=True, blank=True)
     views = models.PositiveIntegerField(default=0)
     price = models.IntegerField(default=0)
     percentage = models.IntegerField(default=0)


     def __str__(self):
          return f'{self.title} - {self.image}'
     

     def save(self, *args, **kwargs):
          if not self.slug:
               self.slug = slugify(self.title,  allow_unicode=True,)
          return super().save(*args, **kwargs)



class Testimonals(BaseModel):
     full_name = models.CharField(max_length=50)
     phone_number = models.CharField(max_length=13)
     image = models.ImageField(upload_to='testimonals_images/')
     message = models.TextField()


     def __str__(self):
          return f'{self.full_name} - {self.phone_number}'



class OrderModel(BaseModel):
     name = models.CharField(max_length=50)
     coffee = models.ForeignKey(CoffeeModel, on_delete=models.CASCADE, related_name='user_coffeess')
     humans = models.CharField(max_length=5, choices=[
          (1,1),
          (2,2),
          (3,3),
          (4,4),
          (5,5),
     ], default=1)
     text = models.CharField(max_length=200)


     def __str__(self):
          return f'{self.name} - {self.humans}'