from django.shortcuts import render
from django.views import View
from .models import CoffeeModel, Testimonals, OrderModel



def HomeView(request):
     coffees = CoffeeModel.objects.all()
     testimonals = Testimonals.objects.filter(is_active=True)
     factik_coffee = CoffeeModel.objects.filter(is_active=True, is_fact=True)
     orders = OrderModel.objects.all()
     context = {
          'coffees': coffees,
          'testimonals': testimonals,
          'factik_coffee': factik_coffee,
          'orders': orders
     }
     return render(request, 'index.html', context)