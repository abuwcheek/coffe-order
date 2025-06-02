from django.contrib import admin
from .models import Blog, Status



@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
     list_display = ('icon', 'name', 'created_at', 'updated_at', 'is_active', 'is_deleted', 'is_featured', 'is_fact', 'is_popular', 'is_trending')
     list_display_links = ('icon', 'name', 'created_at')
     search_fields = ('name',)
     list_filter = ('name',)
     ordering = ('-created_at',)
     list_editable = ('is_active', 'is_deleted', 'is_featured', 'is_fact', 'is_popular', 'is_trending')



@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
     list_display = ('title', 'author', 'status', 'views', 'likes', 'created_at', 'updated_at', 'is_active', 'is_deleted', 'is_featured', 'is_fact', 'is_popular', 'is_trending')
     list_display_links = ('title', 'author')
     search_fields = ('title', 'author')
     list_filter = ('status',)
     ordering = ('-created_at',)
     list_editable = ('status' ,'is_active', 'is_deleted', 'is_featured', 'is_fact', 'is_popular', 'is_trending')
     prepopulated_fields = {'slug': ('title',)}
     readonly_fields = ('views', 'likes')