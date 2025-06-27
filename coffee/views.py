from django.shortcuts import render
from django.views import View
from .models import CoffeeModel, Testimonals, OrderModel
from blog.models import Blog



def HomeView(request):
     coffees = CoffeeModel.objects.all()
     testimonals = Testimonals.objects.filter(is_active=True)
     orders = OrderModel.objects.all()
     
     context = {
          'coffees': coffees,
          'testimonals': testimonals,
          'orders': orders
     }
     return render(request, 'index.html', context)