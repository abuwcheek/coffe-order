from django.db import models

# Create your models here.



class BaseModel(models.Model):
     """
     Base model that provides created_at and updated_at fields.
     """
     created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
     updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")
     is_active = models.BooleanField(default=True, verbose_name="Is Active")
     is_featured = models.BooleanField(default=False, verbose_name="Is Featured")
     is_selling = models.BooleanField(default=False, verbose_name="Is Selling")
     is_fact = models.BooleanField(default=False, verbose_name="Is Fact")
     is_popular = models.BooleanField(default=False, verbose_name="Is Popular")
     is_deleted = models.BooleanField(default=False, verbose_name="Is Deleted")
     is_trending = models.BooleanField(default=False, verbose_name="Is Trending")



     class Meta:
          abstract = True  # This model will not create a table in the database
          ordering = ['-created_at']  # Default ordering by created_at descending