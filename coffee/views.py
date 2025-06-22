from django.shortcuts import render
from django.views import View
from .models import CoffeeModel, Testimonals, OrderModel
from blog.models import Blog



def HomeView(request):
     coffees = CoffeeModel.objects.all()
     factik_blog = Blog.objects.filter(is_active=True, is_fact=True).first()
     testimonals = Testimonals.objects.filter(is_active=True)
     orders = OrderModel.objects.all()
     context = {
          'coffees': coffees,
          'factik_blog': factik_blog,
          'testimonals': testimonals,
          'orders': orders
     }
     return render(request, 'index.html', context)