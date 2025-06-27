from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Blog, Status




class BlogView(View):
     def get(self, request):
          blognews = Blog.objects.filter(is_active=True)
          factik_blog = Blog.objects.filter(is_active=True, is_fact=True)


          context = {
               'blognews': blognews,
               'factik_blog': factik_blog,
          }
          return render(request, 'index.html', context)



class BlogDetailView(View):
     def get(self, request, slug):
          blogdetail = Blog.objects.get(slug=slug)
          blogdetail.views += 1
          blogdetail.save()
          

          context = {
               'blogdetail': blogdetail,
          }
          return render(request, 'blog_detail.html', context)



class BlogFactDetailView(View):
     def get(self, request, slug):
          fact_detail = get_object_or_404(Blog, slug=slug)
          fact_detail.views += 1
          fact_detail.save()

          context = {
               'fact_detail': fact_detail,
          }
          return render(request, 'blog_fact_coffee.html', context)    