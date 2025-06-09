from django.shortcuts import render
from django.views import View
from .models import Blog, Status




class BlogView(View):
     def get(self, request):
          blognews = Blog.objects.filter(is_active=True)

          contex = {
               'blognews': blognews
          }
          return render(request, 'index.html', contex)


class BlogDetailView(View):
     def get(self, request, slug):
          blogdetail = Blog.objects.get(slug=slug)
          blogdetail.views += 1
          blogdetail.save()
          

          context = {
               'blogdetail': blogdetail,
          }
          return render(request, 'blog_detail.html', context)