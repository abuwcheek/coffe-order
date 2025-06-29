from django.urls import path
from .views import BlogView, BlogDetailView, BlogFactDetailView



# blog/urls.py
app_name = 'blog'
urlpatterns = [
     path('', BlogView.as_view(), name='blogurl'),
     path('blog/<slug:slug>/', BlogDetailView.as_view(), name='blogdetailurl'),
     path('blog/fact/<slug:slug>/', BlogFactDetailView.as_view(), name='blogfactdetailurl'),
]