from django.contrib import admin
from .models import CoffeeModel, Testimonals, OrderModel


@admin.register(CoffeeModel)
class CoffeeModelAdmin(admin.ModelAdmin):
     list_display = ('id' ,'title', 'price', 'percentage', 'new_price', 'views', 'status', 'is_active', 'is_deleted', 'is_featured', 'is_fact', 'is_popular', 'is_trending')
     list_display_links = ('id', 'title')
     search_fields = ('title', 'price', 'percentage')
     list_filter = ('status',)
     list_editable = ('status', 'is_active', 'is_deleted', 'is_featured', 'is_fact', 'is_popular', 'is_trending')
     prepopulated_fields = {'slug': ('title',)}
     ordering = ('-created_at',)
     readonly_fields = ('views', )
     fieldsets = (
          (None, {
               'fields': ('title', 'slug', 'description', 'image', 'price', 'percentage', 'views', 'status', 'is_active', 'is_deleted', 'is_featured', 'is_fact', 'is_popular', 'is_trending')
          }),
     )


     def new_price(self, obj):
          return obj.get_new_price



@admin.register(Testimonals)
class TestimonalsAdmin(admin.ModelAdmin):
     list_display = ('id', 'full_name', 'phone_number', 'message', 'is_active', 'is_deleted', 'is_featured', 'is_fact', 'is_popular', 'is_trending')
     list_display_links = ('id', 'full_name')
     search_fields = ('full_name', 'phone_number')
     list_editable = ('is_active', 'is_deleted', 'is_featured', 'is_fact', 'is_popular', 'is_trending')
     ordering = ('-created_at',)
     fieldsets = (
          (None, {
               'fields': ('full_name', 'phone_number', 'message', 'is_active', 'is_deleted')
          }),
     )