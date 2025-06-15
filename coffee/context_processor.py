from .models import CoffeeModel, OrderModel, Testimonals


def index_processor(request):
          coffees = CoffeeModel.objects.all()
          solo_coffee = CoffeeModel.objects.filter(is_active=True, is_popular=True).order_by('?')[:1]
          testimonals = Testimonals.objects.all()
          orders = OrderModel.objects.all()

          
          context = {
               'coffees': coffees,
               'solo_coffee': solo_coffee,
               'testimonals': testimonals,
               'orders': orders
          }
          return context